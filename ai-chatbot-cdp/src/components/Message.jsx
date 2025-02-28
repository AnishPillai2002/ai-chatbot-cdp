const Message = ({ text, isUser, timestamp }) => {
  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div
        className={`max-w-[70%] rounded-lg p-3 ${
          isUser
            ? 'bg-blue-500 text-white rounded-br-none'
            : 'bg-white shadow-md rounded-bl-none'
        }`}
      >
        <p className={`text-sm ${isUser ? 'text-white' : 'text-gray-800'}`}>
          {text}
        </p>
        <p
          className={`text-xs mt-1 ${
            isUser ? 'text-blue-100' : 'text-gray-500'
          }`}
        >
          {timestamp}
        </p>
      </div>
    </div>
  );
};

export default Message; 