from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import asyncio
import os

from screenshot import take_screenshot
from analyzer import analyze_screenshot
from parser import parse_bugs

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "AI Bug Reporter API is running ✅"})

@app.route("/screenshots/<filename>")
def serve_screenshot(filename):
    return send_from_directory("screenshots", filename)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "Please provide a URL"}), 400

    url = data["url"].strip()

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    try:
        local_path, screenshot_url = asyncio.run(take_screenshot(url))
    except Exception as e:
        return jsonify({"error": f"Could not load website: {str(e)}"}), 500

    try:
        raw_response = analyze_screenshot(local_path, url)
    except Exception as e:
        return jsonify({"error": f"AI analysis failed: {str(e)}"}), 500

    bugs = parse_bugs(raw_response)

    return jsonify({
        "url": url,
        "total_bugs": len(bugs),
        "bugs": bugs,
        "screenshot_url": screenshot_url,
        "status": "success"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)