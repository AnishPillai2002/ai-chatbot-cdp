import asyncio
import os
import json
import re
from collections import defaultdict
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter

# Ensure the public folder exists
PUBLIC_FOLDER = os.path.join(os.path.dirname(__file__), "../ai-chatbot-cdp/public")
os.makedirs(PUBLIC_FOLDER, exist_ok=True)

# Paths for storing files
MARKDOWN_FILE = os.path.join(PUBLIC_FOLDER, "markdown.md")
INDEX_FILE = os.path.join(PUBLIC_FOLDER, "index.json")

# List of data sources
DATA_SOURCES = [
    "https://segment.com/docs/",
    "https://docs.mparticle.com/",
    "https://docs.lytics.com/",
    "https://docs.zeotap.com/home/en-us/"
]

async def extract_links(url):
    """Extracts internal links from a webpage."""
    crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url, config=crawl_config)
        if result.success:
            internal_links = [link['href'] for link in result.links.get("internal", [])]
            print(f"\n✅ Extracted {len(internal_links)} internal links from {url}")
            return internal_links
        else:
            print(f"❌ Failed to crawl {url}: {result.error_message}")
            return []

async def generate_markdown(links):
    """Generates Markdown from extracted links and saves it."""
    md_generator = DefaultMarkdownGenerator(
        options={"ignore_links": True, "ignore_images": True, "body_width": 80}
    )
    prune_filter = PruningContentFilter(threshold=0.5, threshold_type="fixed", min_word_threshold=50)
    config = CrawlerRunConfig(markdown_generator=md_generator, content_filter=prune_filter)

    async with AsyncWebCrawler() as crawler:
        markdown_content = ""
        for url in links:
            result = await crawler.arun(url, config=config)
            print(f"📄 Extracting markdown for {url}...")
            if result.success:
                markdown_content += result.markdown + "\n\n---\n\n"
            else:
                print(f"❌ Failed to generate markdown for {url}: {result.error_message}")

        with open(MARKDOWN_FILE, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        print(f"\n✅ Markdown saved to {MARKDOWN_FILE}")

# Document Indexing Functions
def clean_text(text):
    """Cleans text by removing special characters and converting to lowercase."""
    return re.findall(r'\b\w+\b', text.lower())

def index_document():
    """Indexes words along with their line numbers and content from markdown.md."""
    index = defaultdict(list)
    content_by_line = {}

    if not os.path.exists(MARKDOWN_FILE):
        print(f"❌ Error: File '{MARKDOWN_FILE}' not found!")
        return

    with open(MARKDOWN_FILE, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line_number, line in enumerate(lines, start=1):
        words = clean_text(line)
        content_by_line[line_number] = line.strip()
        for word in words:
            index[word].append(line_number)

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump({"index": index, "content": content_by_line}, f, indent=4)

    print("✅ Indexing complete. Saved to", INDEX_FILE)

#Function to search
def search(query):
    """Finds the most relevant lines from the indexed document."""
    query_words = clean_text(query)
    matched_lines = defaultdict(int)
    try:
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            index = data["index"]
            content_by_line = data["content"]

        for word in query_words:
            if word in index:
                for line_number in index[word]:
                    matched_lines[line_number] += 1

        if not matched_lines:
            return "I can't say that."

        sorted_lines = sorted(matched_lines.items(), key=lambda x: x[1], reverse=True)
        relevant_lines = [content_by_line[str(line_num)] for line_num, _ in sorted_lines[:5]]
        return "\n".join(relevant_lines)

    except FileNotFoundError:
        return "I can't say that."

async def main():
    all_links = []
    for source_url in DATA_SOURCES:
        links = await extract_links(source_url)
        all_links.extend(links)

    if all_links:
        print(f"\n🔍 Total links collected: {len(all_links)}")
        await generate_markdown(all_links)
        index_document()  # Call document indexer after markdown generation

if __name__ == "__main__":
    asyncio.run(main())

