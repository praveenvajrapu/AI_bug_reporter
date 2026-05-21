function ScreenshotPanel({ screenshotUrl, url }) {
  return (
    <div className="lg:w-2/5 bg-slate-800 rounded-2xl p-4 flex flex-col gap-3">
      <h2 className="text-white font-semibold text-sm">📸 Website Screenshot</h2>
      <p className="text-slate-500 text-xs truncate">{url}</p>
      <img
        src={screenshotUrl}
        alt="Website Screenshot"
        className="rounded-xl w-full object-cover border border-slate-700"
      />
    </div>
  );
}
export default ScreenshotPanel;