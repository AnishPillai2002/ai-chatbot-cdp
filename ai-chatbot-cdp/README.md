Here’s the **README.md** file in proper Markdown format:  

```markdown
# AI Chatbot with Markdown-Based Knowledge Base

This is an **AI-powered chatbot** that provides responses strictly based on the content of a **Markdown file (`markdown.md`)**. If a user asks a question that is not explicitly mentioned in the Markdown content, the chatbot responds with:

> **"I can't say that."**

## 🚀 Features

- Uses **Azure OpenAI API** for natural language processing.
- Extracts and processes content from a `markdown.md` file.
- Ensures responses are strictly based on the provided Markdown document.
- Implements a **React-based frontend** with a chat UI.
- Provides **real-time AI responses** while restricting hallucinated content.

---

## 🛠 Technologies Used

- **React (Vite)** – Frontend framework for building the UI.
- **Azure OpenAI API** – AI model for generating responses.
- **Tailwind CSS** – For styling and responsive design.
- **Markdown Parsing** – Fetching and processing Markdown content.

---

## 📌 Project Structure

```
ai-chatbot-cdp/
│── public/
│   └── markdown.md  # Knowledge base for the chatbot
│── src/
│   ├── components/
│   │   └── Message.jsx  # Component for displaying messages
│   |   ├── ChatPage.jsx  # Main chat interface
│   ├── App.jsx  # Root component
│   ├── main.jsx  # Entry point
│   └── index.css  # Styling file
│── .env  # Contains API keys (not committed)
│── package.json  # Project dependencies
│── vite.config.js  # Vite configuration
└── README.md  # Project documentation
```

---

## 📌 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-chatbot-cdp.git
cd ai-chatbot-cdp
```

---

### 2️⃣ Install Dependencies

```bash
npm install
```

---

### 3️⃣ Configure Environment Variables

Create a **`.env`** file in the project root and add your **Azure OpenAI API Key**:

```env
VITE_OPENAI_API_KEY=your_openai_api_key_here
```

---

### 4️⃣ Place the Markdown Knowledge Base

Ensure the **`markdown.md`** file is inside the `public/` directory. This file contains the chatbot’s knowledge base.

To generate **markdown.md** run the script.py file in scrapper folder

---

### 5️⃣ Start the Chatbot

Run the chatbot locally using **Vite**:

```bash
npm run dev
```

This will start the chatbot at:

```
http://localhost:5173
```

---

## ℹ️ How It Works

1. The chatbot **fetches** content from the `markdown.md` file when it starts.
2. When a user sends a message, the chatbot:
   - **Checks** if the answer exists in the Markdown content.
   - **Replies** accurately if the content is present.
   - **Returns** "I can't say that." if the answer is unavailable.
3. **Azure OpenAI API** is used to process responses while ensuring strict adherence to the provided Markdown content.

---

## ⚡ Example Usage

- ✅ **User:** "What is AI?"
  - **Chatbot:** "AI stands for Artificial Intelligence. (Based on Markdown content)"
  
- ❌ **User:** "Who is the CEO of Tesla?"
  - **Chatbot:** "I can't say that."

---

## 🛠 Customization

- Modify the **`markdown.md`** file to update the chatbot’s knowledge.
- Adjust the **temperature & max_tokens** values in `ChatPage.jsx` to fine-tune response behavior.
- Change the **UI components** (e.g., message bubbles) inside `Message.jsx`.

---

## 📌 Notes

- The chatbot will **not answer** questions outside of `markdown.md`.
- Ensure the **Azure OpenAI API key** is correct.
- The chatbot can only respond with a maximum of **4096 tokens** due to API constraints.

---

## 🤖 Future Enhancements

- **Improve Markdown parsing** for better response accuracy.
- **Add UI themes** for better user experience.
- **Enable multi-user support** for broader application.

---

🚀 **Now, execute `npm run dev`, and start chatting with your AI chatbot!** 🎉
```
