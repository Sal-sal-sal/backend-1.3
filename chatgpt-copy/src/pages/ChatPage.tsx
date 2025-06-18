import React, { useState, useRef, useEffect } from "react";

const API_URL = "http://localhost:8000/openai";

const ChatPage: React.FC = () => {
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Привет! Я ChatGPT. Чем могу помочь?" },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    const prompt = input.trim();
    if (!prompt) return;
    setMessages((msgs) => [
      ...msgs,
      { role: "user", content: prompt },
    ]);
    setInput("");
    setLoading(true);
    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: prompt }),
      });
      const data = await res.json();
      setMessages((msgs) => [
        ...msgs,
        { role: "assistant", content: data.response },
      ]);
    } catch (err) {
      setMessages((msgs) => [
        ...msgs,
        { role: "assistant", content: "Ошибка при получении ответа от сервера." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 flex flex-col bg-gradient-to-br from-gray-100 to-blue-100">
      <header className="p-6 bg-gradient-to-r from-blue-600 to-blue-400 text-white text-2xl font-bold text-center shadow-md">
        ChatGPT Копия
      </header>
      <main className="flex-1 overflow-y-auto px-6 py-4 space-y-4 scrollbar-thin scrollbar-thumb-blue-200 scrollbar-track-transparent">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}
          >
            <div
              className={`rounded-2xl px-5 py-3 max-w-[70%] text-base shadow-md transition-all duration-200 ${
                msg.role === "user"
                  ? "bg-blue-500 text-white rounded-br-none"
                  : "bg-gray-100 text-gray-900 rounded-bl-none border border-gray-200"
              }`}
            >
              {msg.content}
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </main>
      <form
        onSubmit={sendMessage}
        className="p-4 bg-white flex gap-3 border-t border-gray-200"
        style={{ position: "sticky", bottom: 0, left: 0, right: 0 }}
      >
        <input
          className="flex-1 border border-gray-300 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-400 text-base shadow-sm transition-all text-gray-900 w-full"
          type="text"
          placeholder="Введите сообщение..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          autoFocus
          disabled={loading}
        />
        <button
          type="submit"
          className="bg-blue-500 text-white px-6 py-3 rounded-xl font-semibold hover:bg-blue-600 transition-all shadow-md"
          disabled={loading || !input.trim()}
        >
          {loading ? "..." : "Отправить"}
        </button>
      </form>
    </div>
  );
};

export default ChatPage;
