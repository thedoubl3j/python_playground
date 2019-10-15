from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    greeting = "Hello World"
    return 'Hello, Wo'

if __name__ == "__main__":
    app.run()