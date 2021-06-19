from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        text = function()
        
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye_world():
    return '<h1 style="text-align:center">Bye<h1>''<img src = "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" width=200>'


@app.route("/<name>")
def greet(name):
    return f'Hi {name}!'

if __name__=="__main__":
    # app in debug mode to reload
    app.run(debug=True)