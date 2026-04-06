from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! I am Yuva Rani, learning Flask!"

app.run(debug=True)