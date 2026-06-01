from flask import Flask, request, jsonify
from flask_cors import CORS
import asyncio
import os
import time

from screenshot import take_screenshot
from analyzer import analyze_screenshot
from parser import parse_bugs
from flask import send_from_directory
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "/opt/render/.cache/ms-playwright"


app = Flask(__name__)
CORS(app)  # Allow React frontend to call this API

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "AI Bug Reporter API is running ✅"})

@app.route("/screenshots/<filename>")
def serve_screenshot(filename):
    return send_from_directory("screenshots", filename)


@app.route("/analyze", methods=["POST"])
def analyze():
    """
    Main endpoint.
    Accepts: { "url": "https://example.com" }
    Returns: { "url": ..., "bugs": [...], "screenshot": ..., "total_bugs": ... }
    """

    # ── 1. Validate input ───────────────────────────────────────────
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "Please provide a URL"}), 400

    url = data["url"].strip()

    # Add https:// if missing
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    # ── 2. Take screenshot ──────────────────────────────────────────
    try:
        local_path, screenshot_url = asyncio.run(take_screenshot(url))  # ✅ unpack both
    except Exception as e:
        return jsonify({"error": f"Could not load website: {str(e)}"}), 500

    # ── 3. Analyze with Gemini ──────────────────────────────────────
    try:
        raw_response = analyze_screenshot(local_path, url)  # ✅ pass local path to Gemini
    except Exception as e:
        return jsonify({"error": f"AI analysis failed: {str(e)}"}), 500

    # ── 4. Parse into clean JSON ────────────────────────────────────
    bugs = parse_bugs(raw_response)

    # ── 5. Return response ──────────────────────────────────────────
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

