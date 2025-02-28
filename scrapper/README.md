# Async Web Crawler and Markdown Generator

## Overview
This project is an **asynchronous web crawler** that extracts internal and external links from a given webpage and generates **Markdown documentation** based on the extracted links. The Markdown files are saved in the `public` directory without hyperlinks and images, ensuring clean and readable documentation.

## Features
- Uses `crawl4ai` for efficient asynchronous web crawling.
- Extracts **internal and external links** from a given URL.
- Generates **Markdown** content by crawling linked pages.
- Removes unnecessary elements such as navigation bars and footers using a **content filter**.
- Saves the final Markdown output in the `public` directory inside the ai-chatbot-cdp folder.

## Installation
To use this project, you need to install the required dependencies. Run the following command:

```bash
pip install crawl4ai asyncio
```

## Usage
1. Modify the `website_url` variable in `main()` to set your target website:
    ```python
    website_url = "https://segment.com/docs/"  # Replace with your target website
    ```
2. Run the script:
    ```bash
    python script.py
    ```
3. The extracted Markdown content will be saved in the `public` directory as `markdown.md`.

## File Structure
```
project-folder/
│── ai-chatbot-cdp/
│   └── public/
│       └── markdown.md  # Generated Markdown file
│── scrapper/  # Python Code for Web Scraping
│   ├── app.py
│   └── requirements.txt  # Dependencies

```

## Configuration
The Markdown generation is configured with:
- **Ignoring hyperlinks and images** to keep content clean.
- **PruningContentFilter** to remove unnecessary sections like navigation and footers.
- **Body width of 80 characters** for better readability.

## Dependencies
- `crawl4ai`
- `asyncio`
- `os`


## How It Works
-The scraper extracts webpage content and converts it into Markdown format.

-The chatbot uses this Markdown as its knowledge base, responding strictly based on its content.

-If a user asks something not present in markdown.md, the chatbot replies with "I can't say that."
