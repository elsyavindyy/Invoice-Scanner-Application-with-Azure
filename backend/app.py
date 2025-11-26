from flask import Flask, request, jsonify
from flask_cors import CORS
from azure_engine import run_scan
import os

app = Flask(__name__)
CORS(app) 
@app.route("/scan", methods=["POST"])
def ocr():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]
        filepath = os.path.join("uploads", file.filename)
        file.save(filepath)
        print("📌 File saved:", filepath)
        # LANGSUNG RETURN JSON STRING
        result_dict = run_scan(filepath)
        print("📌 OCR result:", result_dict)
        return jsonify(result_dict)

    except Exception as e:
        # print full stack trace
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
