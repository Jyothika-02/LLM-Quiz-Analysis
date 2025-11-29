from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

SECRET = "your-secret-string"

@app.route("/", methods=["POST"])
def main():

    # 1. Validate JSON
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    # 2. Validate secret
    if data.get("secret") != SECRET:
        return jsonify({"error": "Forbidden"}), 403

    # 3. Get quiz URL
    url = data.get("url")
    if not url:
        return jsonify({"error": "Missing URL"}), 400

    # 4. Visit quiz page
    page = requests.get(url).text

    # 5. Extract question text
    soup = BeautifulSoup(page, "html.parser")
    question = soup.get_text()

    # 6. Very basic: just reply placeholder
    answer = "dummy-answer"

    return jsonify({
        "email": data["email"],
        "secret": SECRET,
        "url": url,
        "answer": answer
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
