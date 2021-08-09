import re
from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)



def get_age(name,parameters):
    response_age = requests.get(url='https://api.agify.io/',params=parameters)
    return response_age.json().get('age')

def get_gender(name,parameters):
    response_gender = requests.get(url = 'https://api.genderize.io/',params=parameters)
    return response_gender.json().get('gender')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/guess/<string:name>")
def guess(name):
    parameters = {"name" : name}
    age = get_age(name,parameters)
    gender = get_gender(name,parameters)
    return render_template("output.html",name = name.title(),age = age,gender= gender)

@app.route('/blog/<num>')
def blogs(num):
    print(num)
    response = requests.get(url='https://api.npoint.io/47f6f231d03ed60985ba')
    all_posts = response.json()
    print(all_posts)
    return render_template('blog.html', posts = all_posts)

if __name__=="__main__":
    app.run(debug=True)