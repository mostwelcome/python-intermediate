from flask import Flask
from flask import render_template
from random import randint
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello():
    number = randint(1,10)
    current_year = date.today().year
    # pass values inside html with unlimited keyword arguments 
    return render_template("index.html",num = number,year = current_year)


if __name__ == "__main__":
    app.run(debug=True)