from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Shivani is the best partner!'
