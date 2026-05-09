function ScreenshotPanel({ screenshotPath, url }) {
  // Convert backend path to filename only
  const filename = screenshotPath?.split("/").pop() ||
                   screenshotPath?.split("\\").pop();

  return (
    <div className="lg:w-2/5 bg-slate-800 rounded-2xl p-4 flex flex-col gap-3">
      <h2 className="text-white font-semibold text-sm">📸 Website Screenshot</h2>
      <p className="text-slate-500 text-xs truncate">{url}</p>

      {/* Serve screenshot from Flask static route */}
      <img
        src={`http://127.0.0.1:5000/screenshots/${filename}`}
        alt="Website Screenshot"
        className="rounded-xl w-full object-cover border border-slate-700"
        onError={(e) => {
          e.target.style.display = "none";
        }}
      />
    </div>
  );
}

export default ScreenshotPanel;