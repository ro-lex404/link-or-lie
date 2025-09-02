from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/')
def phish():
    return render_template("index.html")

@app.route('/spot-the-phish')
def game():
    return render_template("spot-the-phish.html")

@app.route('/process-form', methods=['POST'])
def process_form():
    link = request.form.get("link")
    retVal = model.model(link)

    return retVal

if __name__ == "__main__":
    app.run(debug=True)