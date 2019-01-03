
from flask import Flask
app = Flask(__name__)

@app.route("/")
def greeting():
    return "<h>Hello World!</h1>"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
