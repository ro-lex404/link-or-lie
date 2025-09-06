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

@app.route('/process-form', methods=['GET','POST'])
def form():
    try:
        if request.method == 'POST':
            link = request.form.get('link')
            if not link:
                return jsonify({"error": "No link provided"}), 400
            print(f"Received link: {link}")  # Debug logging
            retVal = linkModel.model(link)
            return jsonify({"result": retVal})  # Wrap the response in a JSON object
        else:
            link = request.args.get('link')
            if not link:
                return jsonify({"error": "No link provided"}), 400
            retVal = linkModel.model(link)
            return jsonify({"result": retVal})
    except ConnectionError:
        return jsonify({"error": "Please check your internet connection"}), 503
    
@app.route("/get-links")
def get_links():
    options = gameModel.get_random_links()
    return jsonify(options)

if __name__ == "__main__":
    app.run(debug=True)