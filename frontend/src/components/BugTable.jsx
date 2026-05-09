const severityStyles = {
  High:   "bg-red-900/50 text-red-300 border border-red-700",
  Medium: "bg-yellow-900/50 text-yellow-300 border border-yellow-700",
  Low:    "bg-green-900/50 text-green-300 border border-green-700",
};

const severityIcon = {
  High: "🔴",
  Medium: "🟡",
  Low: "🟢",
};

function BugTable({ bugs }) {
  if (bugs.length === 0) {
    return (
      <div className="flex-1 bg-slate-800 rounded-2xl p-8 flex items-center
                      justify-center text-green-400 text-lg font-semibold">
        ✅ No visual bugs found! Website looks great.
      </div>
    );
  }

  return (
    <div className="flex-1 bg-slate-800 rounded-2xl p-4 flex flex-col gap-3 overflow-y-auto max-h-[600px]">
      <h2 className="text-white font-semibold text-sm">
        🐛 Bug Report ({bugs.length} issues found)
      </h2>

      {bugs.map((bug, index) => (
        <div
          key={index}
          className="bg-slate-900 rounded-xl p-4 flex flex-col gap-2
                     border border-slate-700 hover:border-slate-500 transition"
        >
          {/* Title + Severity */}
          <div className="flex items-center justify-between gap-2">
            <p className="text-white font-semibold text-sm">{bug.title}</p>
            <span className={`text-xs px-2 py-1 rounded-full font-medium whitespace-nowrap
                             ${severityStyles[bug.severity]}`}>
              {severityIcon[bug.severity]} {bug.severity}
            </span>
          </div>

          {/* Location */}
          <p className="text-slate-500 text-xs">
            📍 {bug.location}
          </p>

          {/* Description */}
          <p className="text-slate-300 text-xs leading-relaxed">
            {bug.description}
          </p>

          {/* Fix */}
          <div className="bg-blue-900/30 border border-blue-800 rounded-lg px-3 py-2">
            <p className="text-blue-300 text-xs">
              💡 <span className="font-medium">Fix:</span> {bug.fix}
            </p>
          </div>
        </div>
      ))}
    </div>
  );
}

export default BugTable;