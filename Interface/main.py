from flask import Flask,render_template,request,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


#Create a flask instance


app = Flask(__name__)

@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html',title=title)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/about')
def about():
    title = 'About'
    return render_template('about.html',title=title)

@app.route('/contact')
def contact():
    title = 'Contact'
    return render_template('contact.html',title=title)

@app.route('/dashboard')
def dashboard():
    title = 'Dashboard'
    return render_template('dashboard.html',title=title)

@app.route('/blogs')
def blog():
    title = 'Blogs'
    return render_template('blog.html',title=title)

@app.route('/blog/<int:id>/')
def post(id):
    title = 'Blog'

    return render_template('post.html',title=title)


if __name__ == "__main__":
    
    app.run(debug=True, host='0.0.0.0', port=8080)