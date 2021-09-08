from flask import Flask,render_template,request,redirect
from flask.helpers import url_for
import sqlite3

app = Flask(__name__)

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title VARCHAR(250) NOT NULL UNIQUE,author VARCHAR(250) NOT NULL,rating FLOAT NOT NULL)')

all_books = []

@app.route('/')
def home():
    return render_template('index.html',books=all_books)

@app.route('/add',methods = ['GET','POST'])
def add_book():
    if request.method == 'POST':
        new_book = {
            'title': request.form['name'],
            'author':request.form['author'],
            'rating':request.form['rating']
        }
        all_books.append(new_book)
        print(all_books)
        return redirect(url_for('home'))
    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(debug=True)