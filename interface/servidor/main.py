from flask import Flask, render_template
import data_generator as dg
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=dg.generator())

if __name__ == '__main__':
    print(dg.generator())
    app.run('127.0.0.1',5000,debug=True)

    