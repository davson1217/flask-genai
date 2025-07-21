from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.error_codes import UNSUPPORTED_MEDIA_TYPE, CLIENT_BAD_REQUEST, INTERNAL_SERVER_ERROR, make_response
from genai.openrouter import OpenRouter

app = Flask(__name__)

CORS(app)

chat_model = OpenRouter()  # default

@app.before_request
def require_json():
    if request.method == "POST" and not request.is_json:
        return jsonify({"error": "Request must be json"}), UNSUPPORTED_MEDIA_TYPE


@app.route("/")
def index():
    return "Hello stanger"

@app.route("/prompt", methods=["OPTIONS"])
def handle():
    return "OK", 200

@app.route("/prompt", methods=["POST"])
def handle_prompt():
    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Missing prompt"}), CLIENT_BAD_REQUEST
    
    try:
        result = chat_model.generate_response(prompt)

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), INTERNAL_SERVER_ERROR

if __name__ == "__main__":
    app.run(debug=True)