from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1 style= "text-align: centre"> hello world </h1>'


@app.route('/bye')
def bye():
    return "bye"


@app.route("/userName/<name>/<int:number>")
def greet(name, number):
    return f"hello there {name}, you are {number} years old"



if __name__ == '__main__':
    app.run(debug=True)