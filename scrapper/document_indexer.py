import os
import json
import re
from collections import defaultdict
from difflib import SequenceMatcher

def clean_text(text):
    """Cleans text by removing special characters and converting to lowercase."""
    return re.findall(r'\b\w+\b', text.lower())

def index_document(file_path):
    """Indexes words along with their line numbers from markdown.md."""
    index = defaultdict(list)

    if not os.path.exists(file_path):
        print(f"❌ Error: File '{file_path}' not found!")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line_number, line in enumerate(lines, start=1):  # Start from line 1
        words = clean_text(line)
        for word in words:
            index[word].append(line_number)  # Store occurrences

    with open("index.json", "w", encoding="utf-8") as f:
        json.dump(index, f, indent=4)

    print("✅ Indexing complete. Saved to index.json")

def search(query):
    """Searches for the query in the indexed document and returns the best-matching lines."""
    query_words = clean_text(query)  # Normalize query
    matched_lines = defaultdict(int)  # Line number -> match score

    try:
        with open("index.json", "r", encoding="utf-8") as f:
            index = json.load(f)

        # Find matching line numbers
        for word in query_words:
            if word in index:
                for line_number in index[word]:
                    matched_lines[line_number] += 1  # Increase match score

        if not matched_lines:
            print(f"❌ No relevant lines found for '{query}'.")
            return

        # Sort by highest match score
        sorted_lines = sorted(matched_lines.items(), key=lambda x: x[1], reverse=True)

        print(f"\n📌 Top matching lines for '{query}':")
        for line_num, score in sorted_lines[:5]:  # Return top 5 matches
            print(f"  - Line {line_num} (score: {score})")

    except FileNotFoundError:
        print("❌ Index not found. Run indexing first.")

if __name__ == "__main__":
    markdown_path = "../ai-chatbot-cdp/public/markdown.md"
    index_document(markdown_path)

    while True:
        query = input("\nEnter a question to search (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        search(query)
