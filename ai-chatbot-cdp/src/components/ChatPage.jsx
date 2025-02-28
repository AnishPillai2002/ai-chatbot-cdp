import { useState, useRef, useEffect } from "react";
import Message from "./Message";
import OpenAI from "openai";

const ChatPage = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [indexData, setIndexData] = useState(null);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    const fetchIndex = async () => {
      try {
        const response = await fetch("/index.json");
        const data = await response.json();
        setIndexData(data);
      } catch (error) {
        console.error("Error fetching index.json:", error);
      }
    };
    fetchIndex();
  }, []);

  const searchRelevantContext = (query) => {
    console.log("Query:", query)
    console.log("Index Data",indexData)
    if (!indexData) return "I can't say that.";
    
    const words = query.toLowerCase().match(/\b\w+\b/g) || [];
    const matchedLines = {};

    words.forEach((word) => {
      if (indexData.index[word]) {
        indexData.index[word].forEach((line) => {
          matchedLines[line] = (matchedLines[line] || 0) + 1;
        });
      }
    });

    if (Object.keys(matchedLines).length === 0) return "I can't say that.";

    const sortedLines = Object.entries(matchedLines).sort((a, b) => b[1] - a[1]);
    const relevantLines = sortedLines.slice(0, 5).map(([line]) => indexData.content[line]);

    return relevantLines.join("\n");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { text: input, isUser: true, timestamp: new Date().toLocaleTimeString() };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsLoading(true);

    try {
      const openai = new OpenAI({
        baseURL: "https://models.inference.ai.azure.com",
        apiKey: import.meta.env.VITE_OPENAI_API_KEY,
        dangerouslyAllowBrowser: true,
      });

      const relevantContext = searchRelevantContext(input);

      console.log("Relevant Context:", relevantContext);

      const response = await openai.chat.completions.create({
        model: "gpt-4o",
        messages: [
          {
            role: "system",
            content: `You are a strict assistant that only provides answers based on the provided Markdown document.
      
      Your knowledge is limited to the content extracted from the Markdown file. If a user asks a question that is not directly answered in the Markdown content, reply with:
      "I can't say that."
      
      Context: Here is the only information you know:
      ${relevantContext}
      
      Remember:
      - If the relevantContext is not empty, respond accurately with text only avoiding unnecessary links.
      - If the answer is partially available in the relevantContext, explain in easy to understand way.
      - If the answer is completely unavailable in relevantContext, respond with: "I can't say that."
      - Do not generate or assume information beyond the relevantContext.`,
          },
          { role: "user", content: input },
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
      console.error("Error:", error);
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
