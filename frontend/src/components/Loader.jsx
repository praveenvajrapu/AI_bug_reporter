function Loader() {
  return (
    <div className="flex flex-col items-center justify-center mt-16 gap-4">
      {/* Spinner */}
      <div className="w-14 h-14 border-4 border-slate-700 border-t-blue-500
                      rounded-full animate-spin" />
      <p className="text-slate-400 text-sm animate-pulse">
        Taking screenshot & analyzing with AI... this may take 10–20 seconds
      </p>
    </div>
  );
}

export default Loader;