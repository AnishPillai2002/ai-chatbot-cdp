import os
import json
import re
from collections import defaultdict

def clean_text(text):
    """Cleans text by removing special characters and converting to lowercase."""
    return re.findall(r'\b\w+\b', text.lower())

def index_document(file_path, index_path):
    """Indexes words along with their line numbers and content from markdown.md."""
    index = defaultdict(list)
    content_by_line = {}

    if not os.path.exists(file_path):
        print(f"❌ Error: File '{file_path}' not found!")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line_number, line in enumerate(lines, start=1):  # Start from line 1
        words = clean_text(line)
        content_by_line[line_number] = line.strip()  # Store the actual content of each line
        for word in words:
            index[word].append(line_number)  # Store occurrences

    # Save index and content
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump({"index": index, "content": content_by_line}, f, indent=4)

    print("✅ Indexing complete. Saved to", index_path)

def search(query, index_path):
    """Finds the most relevant lines from the indexed document."""
    query_words = clean_text(query)
    matched_lines = defaultdict(int)

    try:
        with open(index_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            index = data["index"]
            content_by_line = data["content"]

        # Find matching line numbers
        for word in query_words:
            if word in index:
                for line_number in index[word]:
                    matched_lines[line_number] += 1  # Increase match score

        if not matched_lines:
            return "I can't say that."

        # Sort by highest match score
        sorted_lines = sorted(matched_lines.items(), key=lambda x: x[1], reverse=True)

        # Retrieve top relevant content
        relevant_lines = [content_by_line[str(line_num)] for line_num, _ in sorted_lines[:5]]
        return "\n".join(relevant_lines)

    except FileNotFoundError:
        return "I can't say that."

if __name__ == "__main__":
    markdown_path = "../ai-chatbot-cdp/public/markdown.md"  # Adjust path if needed
    index_path = "../ai-chatbot-cdp/public/index.json"  # Store in public folder

    index_document(markdown_path, index_path)
