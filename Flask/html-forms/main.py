from flask import Flask,request,redirect,url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST'])
def login():
    user = request.form['name']
    password = request.form['password']
    # return redirect(url_for('success',name = user))
    return render_template("output.html",user_name = user, password = password)
   
if __name__=="__main__":
    app.run(debug=True)