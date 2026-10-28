from flask import Flask
import os  # <-- Import the operating system library

app = Flask(__name__)


@app.route("/")
def hello_world():
    # Read 'CUSTOM_MESSAGE'. If it doesn't exist, fall back to a default string.
    message = os.getenv("CUSTOM_MESSAGE", "Hello, World!")
    return f"<h1>{message}</h1>"

@app.route('/api/greet', methods=['GET'])
def greet_user():
    return {"message": "Hello from src repo!!", "status": "success"}, 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
