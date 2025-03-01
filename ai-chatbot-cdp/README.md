# AI Chatbot

## Overview

This AI-powered chatbot leverages OpenAI's GPT-4o model to generate responses strictly based on a predefined Markdown document. The chatbot fetches relevant context from the Markdown file, ensuring it does not hallucinate or answer questions beyond the provided context.

## Approach

-   The chatbot integrates OpenAI's GPT-4o for generating responses.
-   A web-scraping script (`web_scraping_script.py`) extracts relevant information and stores it in `markdown.md`.
-   When a user asks a question, the chatbot searches the Markdown file for relevant context.
-   A well-structured prompt, including the extracted context, is passed to GPT-4o to ensure precise responses.
-   If no relevant context is found, the chatbot responds with: **"I can't say that."**

## Technologies Used

-   **React.js** - For building the front-end user interface.
-   **Vite** - For fast and optimized React development.
-   **Tailwind CSS** - For styling and responsive design.
-   **OpenAI API** - To generate contextually accurate responses.

## Setting Up the Project

1.  Clone the repository:
    
    ```sh
    git clone https://github.com/AnishPillai2002/ai-chatbot-cdp.git
    cd ai-chatbot-cdp
    
    ```
    
2.  Install dependencies:
    
    ```sh
    npm install
    
    ```
    
3.  Set environment variables in a `.env` file:
    
    ```sh
    VITE_OPENAI_API_KEY=your_openai_api_key_here
    
    ```
    
4.  Start the development server:
    
    ```sh
    npm run dev
    
    ```
    

## Future Enhancements

-   Implementing automated context updates using more advanced web scraping techniques.
-   Utilizing a more powerful LLM with a higher token limit for better response generation.
-   Enhancing the chatbot's ability to process longer queries while maintaining response accuracy.