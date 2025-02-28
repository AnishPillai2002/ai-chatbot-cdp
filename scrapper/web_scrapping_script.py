import asyncio
import os
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter

# Ensure the public folder exists
PUBLIC_FOLDER = os.path.join(os.path.dirname(__file__), "../ai-chatbot-cdp/public")
os.makedirs(PUBLIC_FOLDER, exist_ok=True)

async def extract_links(url):
    """Extracts internal and external links from a webpage."""
    crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url, config=crawl_config)

        if result.success:
            internal_links = [link['href'] for link in result.links.get("internal", [])]
            external_links = [link['href'] for link in result.links.get("external", [])]

            print("\nInternal Links:", internal_links[:10])  # Show first 10 links
            print("\nExternal Links:", external_links[:10])

            return internal_links  # Returning extracted links
        else:
            print("Crawl failed:", result.error_message)
            return []

async def generate_markdown(links):
    """Generates Markdown for the first 10 extracted links and saves it without links or images."""

    # Configure the Markdown Generator to ignore links and images
    md_generator = DefaultMarkdownGenerator(
        options={
            "ignore_links": True,  # Remove hyperlinks
            "ignore_images": True,  # Remove images
            "body_width": 80  # Keep lines wrapped at 80 characters
        }
    )

    # Use PruningContentFilter to remove unnecessary content like navigation, footers
    prune_filter = PruningContentFilter(
        threshold=0.5,
        threshold_type="fixed",
        min_word_threshold=50
    )

    config = CrawlerRunConfig(
        markdown_generator=md_generator,
        content_filter=prune_filter
    )

    async with AsyncWebCrawler() as crawler:
        markdown_content = ""
        for url in links[:20]:  # Limit to first 20 links
            result = await crawler.arun(url, config=config)
            print(f"Extracting markdown for {url}...")

            if result.success:
                markdown_content += result.markdown + "\n\n---\n\n"
            else:
                print(f"Failed to generate markdown for {url}: {result.error_message}")

        # Save the Markdown file in the public folder
        markdown_file = os.path.join(PUBLIC_FOLDER, "markdown.md")
        with open(markdown_file, "w", encoding="utf-8") as f:
            f.write(markdown_content)

        print(f"\nMarkdown generation completed. Saved to {markdown_file}")

async def main():
    website_url = "https://segment.com/docs/"  # Replace with your target website
    internal_links = await extract_links(website_url)

    if internal_links:
        print("\nGenerating Markdown for first 10 links...\n")
        await generate_markdown(internal_links)

if __name__ == "__main__":
    asyncio.run(main())
