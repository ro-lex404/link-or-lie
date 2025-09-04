from flask import Flask, render_template, request
import linkModel

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
    except ConnectError as e:
        return "Please check your internet connection and try again."

if __name__ == "__main__":
    app.run(debug=True)