from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def phish():
    return render_template("index.html")

@app.route('/spot-the-phish')
def game():
    return render_template("spot-the-phish.html")

if __name__ == "__main__":
    app.run(debug=True)