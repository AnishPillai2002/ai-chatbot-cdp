import { useState, useRef, useEffect } from 'react';
import Message from './Message';
import OpenAI from "openai";

const ChatPage = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [markdownContent, setMarkdownContent] = useState(""); // State to store Markdown content
  const messagesEndRef = useRef(null);

  useEffect(() => {
    const fetchMarkdown = async () => {
      try {
        const response = await fetch("/markdown.md"); // Ensure the markdown file is accessible
        const text = await response.text();
        console.log(text);
        setMarkdownContent(text.slice(0, 2000)); // Limiting characters to fit model constraints
      } catch (error) {
        console.error("Error fetching Markdown file:", error);
      }
    };
    fetchMarkdown();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { text: input, isUser: true, timestamp: new Date().toLocaleTimeString() };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      const openai = new OpenAI({
        baseURL: "https://models.inference.ai.azure.com",
        apiKey: import.meta.env.VITE_OPENAI_API_KEY,
        dangerouslyAllowBrowser: true,
      });

      const response = await openai.chat.completions.create({
        model: "gpt-4o",
        messages: [
          {
            role: "system",
            content: `You are a strict assistant that only provides answers based on the provided Markdown document. 
      
      Your knowledge is limited to the content extracted from the Markdown file. If a user asks a question that is not directly answered in the Markdown content, reply with:
      "I can't say that."
      
      Context: Here is the only information you know:
      ${markdownContent}
      
      Remember:
      - If the answer is explicitly in the Markdown file, respond accurately.
      - If the answer is partially available, state only what is known from the Markdown.
      - If the answer is completely unavailable, respond with: "I can't say that."
      - Do not generate or assume information beyond the Markdown content.`
          },
          { role: "user", content: input }
        ],
        temperature: 1,
        max_tokens: 4096,
        top_p: 1,
      });

      const aiMessage = {
        text: response.choices[0].message.content,
        isUser: false,
        timestamp: new Date().toLocaleTimeString(),
      };
      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-gray-100">
      <div className="flex-none bg-white shadow-md p-4">
        <h1 className="text-2xl font-bold text-center text-gray-800">AI Chatbot</h1>
      </div>
      
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((message, index) => (
          <Message key={index} {...message} />
        ))}
        {isLoading && (
          <div className="flex justify-start">
            <div className="bg-gray-200 rounded-lg p-3 animate-pulse">
              <span className="text-gray-500">AI is thinking...</span>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <form onSubmit={handleSubmit} className="flex-none p-4 bg-white shadow-md">
        <div className="flex space-x-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your message..."
            className="flex-1 p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            type="submit"
            disabled={isLoading}
            className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50"
          >
            {isLoading ? "Thinking..." : "Send"}
          </button>
        </div>
      </form>
    </div>
  );
};

export default ChatPage;
