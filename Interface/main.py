from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html',title=title)

@app.route('/about')
def about():
    title = 'About'
    return render_template('about.html',title=title)

@app.route('/contact')
def contact():
    title = 'Contact'
    return render_template('contact.html',title=title)

@app.route('/blog')
def blog():
    title = 'Blog'
    return render_template('blog.html',title=title)


if __name__ == "__main__":
    
    app.run(debug=True, host='0.0.0.0', port=8080)