import { useState } from "react";
import Header from "./components/Header";
import UrlInput from "./components/UrlInput";
import Loader from "./components/Loader";
import ScreenshotPanel from "./components/ScreenshotPanel";
import BugTable from "./components/BugTable";

function App() {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleAnalyze = async () => {
    // Validate
    if (!url.trim()) {
      setError("Please enter a website URL");
      return;
    }

    setError("");
    setResult(null);
    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });

      const data = await response.json();

      if (!response.ok) {
        setError(data.error || "Something went wrong");
      } else {
        setResult(data);
      }
    } catch (err) {
      setError("Cannot connect to backend. Make sure Flask is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen px-6 py-8 max-w-7xl mx-auto">
      <Header />

      <UrlInput
        url={url}
        setUrl={setUrl}
        onAnalyze={handleAnalyze}
        loading={loading}
      />

      {error && (
        <div className="mt-4 p-4 bg-red-900/40 border border-red-500 
                        rounded-lg text-red-300 text-sm">
          ⚠️ {error}
        </div>
      )}

      {loading && <Loader />}

      {result && (
        <div className="mt-8 flex flex-col gap-8">
          {/* Summary bar */}
          <div className="flex gap-6">
            <div className="bg-slate-800 rounded-xl px-6 py-4 text-center">
              <p className="text-3xl font-bold text-white">{result.total_bugs}</p>
              <p className="text-slate-400 text-sm mt-1">Total Bugs Found</p>
            </div>
            <div className="bg-slate-800 rounded-xl px-6 py-4 text-center">
              <p className="text-3xl font-bold text-red-400">
                {result.bugs.filter(b => b.severity === "High").length}
              </p>
              <p className="text-slate-400 text-sm mt-1">High Severity</p>
            </div>
            <div className="bg-slate-800 rounded-xl px-6 py-4 text-center">
              <p className="text-3xl font-bold text-yellow-400">
                {result.bugs.filter(b => b.severity === "Medium").length}
              </p>
              <p className="text-slate-400 text-sm mt-1">Medium Severity</p>
            </div>
            <div className="bg-slate-800 rounded-xl px-6 py-4 text-center">
              <p className="text-3xl font-bold text-green-400">
                {result.bugs.filter(b => b.severity === "Low").length}
              </p>
              <p className="text-slate-400 text-sm mt-1">Low Severity</p>
            </div>
          </div>

          {/* Screenshot + Bug Table side by side */}
          <div className="flex flex-col lg:flex-row gap-6">
            <ScreenshotPanel screenshotPath={result.screenshot_path} url={result.url} />
            <BugTable bugs={result.bugs} />
          </div>
        </div>
      )}
    </div>
  );
}

export default App;