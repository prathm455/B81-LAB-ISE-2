
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Student Performance Prediction</h1>"

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
