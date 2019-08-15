import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/ur namae')
def name():
    return 'I am simple webapp!' 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
