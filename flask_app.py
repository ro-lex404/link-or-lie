from flask import Flask, jsonify, render_template, request
import linkModel, gameModel
from requests.exceptions import ConnectionError

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/spot-the-phish')
def game():
    return render_template("spot-the-phish.html")

@app.route('/process-form', methods=["POST"])
def form():
    try:
        link = request.form.get("link")
        retVal = linkModel.model(link)
        return retVal
    except ConnectionError:
        return "Please check your internet connection and try again."

@app.route("/get-links")
def get_links():
    options = gameModel.get_random_links()
    return jsonify(options)

if __name__ == "__main__":
    app.run(debug=True)