# Web Scraping & Document Indexing

## Overview

This script performs web scraping on specified data sources, extracts content, generates a Markdown file, indexes the content, and allows searching through the indexed data. It utilizes **Crawl4AI** for scraping.

## Features

-   **Web Scraping:** Extracts documentation from predefined sources.
-   **Markdown Generation:** Converts scraped content into a structured Markdown file.
-   **Indexing:** Stores indexed words along with their occurrences for efficient searching.
-   **Search Functionality:** Finds relevant content based on user queries.(Currently not being used, can be used in future versions of this project)

## Technologies & Dependencies

-   **Python 3.x**
-   **Crawl4AI** (for web scraping)
-   **Asyncio** (for asynchronous operations)
-   **JSON** (for data storage)
-   **Regular Expressions** (for text processing)
-   **Collections (defaultdict)** (for indexing data)

### Install Dependencies

Ensure you have Python 3 installed. Then, install the required packages:

```sh
pip install crawl4ai asyncio

```

Alternatively, if using a **virtual environment**, follow these steps:

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
pip install -r requirements.txt

```

### Install Dependencies

1.  **Extracts internal links** from the predefined documentation sources.
2.  **Generates Markdown** from the extracted content.
3.  **Indexes the document** for efficient text search.
4.  **Enables search functionality** to find the most relevant lines based on user queries.


## File Structure

-   `markdown.md` → Contains structured scraped content.
-   `index.json` → Stores indexed content for quick search.

Both these files will be stored in ai-chatbot-cdp/public folder.


## Future Enhancements

-   Implementing a database for persistent storage.
-   Adding multi-language support.
-   Improving indexing using **Retrieval-Augmented Generation (RAG)**.
-   Hosting **DeepSeek** to improve token limits for better search results.



### 🚀 Built for Efficient Data Extraction & Retrieval