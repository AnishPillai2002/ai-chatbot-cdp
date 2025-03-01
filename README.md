# AI Chatbot with Document Indexing and Web Scraping

## Overview

This project is an AI-powered chatbot that provides relevant answers based on indexed documentation. It extracts content from various sources using a Python web scraping script, processes the data into a structured format, and utilizes OpenAI to generate responses based on user queries.

## Approach

The project follows a structured approach to ensure efficient data retrieval and response generation:

1.  **Frontend Development:**
    
    -   Developed using **React.js** for a dynamic and interactive user experience.
        
    -   Styled using **Tailwind CSS** to ensure a clean and responsive UI.
        
2.  **Data Extraction & Processing:**
    
    -   A **Python web scraping script** powered by **Crawl4AI**  extracts content from various documentation sources:
        
        -   [Segment Documentation](https://segment.com/docs/?ref=nav)
            
        -   [mParticle Documentation](https://docs.mparticle.com/)
            
        -   [Lytics Documentation](https://docs.lytics.com/)
            
        -   [Zeotap Documentation](https://docs.zeotap.com/home/en-us/)
            
    -   The extracted data is stored in a **Markdown file**((ai-chatbot-cdp\public\markdown.md)) for structured indexing.
        
3.  **Document Indexing:**
    
    -   The scraped content is **indexed** for efficient retrieval based on keywords and phrases.
        
    -   The chatbot processes user queries and searches for **relevant content** in the indexed documentation (ai-chatbot-cdp\public\index.json).
        
4.  **AI-Powered Responses:**
    
    -   Uses **OpenAI API** to generate intelligent responses based on indexed data.
        
    -   Ensures that responses strictly adhere to the extracted documentation content.

## Steps

1.  **Clone the repository:**
    
    ```
    git clone https://github.com/AnishPillai2002/ai-chatbot-cdp.git
    
    ```
    
2.  **Run the Scraper:**
    
    ***Prerequisites**

    Ensure you have the following installed:

-   Python 3.8 or later
-   Playwright
-   Chromium browser
    

    
    ```sh
    cd scrapper
    pip install -r requirements.txt 
    playwright install chromium
    python web_scrapping_script.py
    ```
    
    -   This script scrapes all data from the source websites and stores it in `markdown.md` inside the `ai-chatbot-cdp/public` folder.
        
    -   It also generates `index.json`, which indexes the Markdown content for efficient retrieval based on user queries.

    Alternatively, if using a **virtual environment**, follow these steps:

    ```sh
    cd scrapper
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    pip install -r requirements.txt
    playwright install chromium
    python web_scrapping_script.py
    ```
        
3.  **Start the Chatbot:**
    
    ```
    cd ai-chatbot-cdp
    npm install
    npm run dev
    ```
    

### Important Notes

-   The chatbot will function properly **only after** running `web_scrapping_script.py`.
    
-   It will **not** answer random questions unrelated to the content inside `markdown.md` in `ai-chatbot-cdp/public`.


## Future Enhancements
-   Improve search algorithms for more accurate context retrieval.
    
-   Use an improved version of document indexing to extract relevant data.
    
-   Host **DeepSeek** to improve the token limit for better responses.
    
-   Explore possibilities of **Retrieval-Augmented Generation (RAG)** for more accurate context-driven answers.