
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Student Performance Prediction</h1>
    <p>Enter your daily study hours.</p>
    <form action="/predict" method="get">
        <label>Study hours:</label>
        <input type="number" name="hours" min="0" max="24"
               step="0.5" required>
        <button type="submit">Predict</button>
    </form>
    """


@app.route("/predict")
def predict():
    try:
        hours = float(request.args.get("hours", ""))
    except ValueError:
        return "Enter valid study hours", 400

    if not 0 <= hours <= 24:
        return "Study hours must be between 0 and 24", 400

    if hours >= 6:
        result = "Good performance expected"
    else:
        result = "More study practice recommended"

    return f"<h2>{result}</h2><a href='/'>Go back</a>"


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
