function UrlInput({ url, setUrl, onAnalyze, loading }) {
  const handleKeyDown = (e) => {
    if (e.key === "Enter") onAnalyze();
  };

  return (
    <div className="flex flex-col sm:flex-row gap-3 w-full">
      <input
        type="text"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="Enter website URL... e.g. https://example.com"
        className="flex-1 px-5 py-4 rounded-xl bg-slate-800 border border-slate-600
                   text-white placeholder-slate-500 text-sm outline-none
                   focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition"
      />
      <button
        onClick={onAnalyze}
        disabled={loading}
        className="px-8 py-4 bg-blue-600 hover:bg-blue-500 disabled:bg-blue-900
                   disabled:cursor-not-allowed text-white font-semibold rounded-xl
                   transition text-sm whitespace-nowrap"
      >
        {loading ? "Analyzing..." : "🔍 Analyze"}
      </button>
    </div>
  );
}

export default UrlInput;