from flask import Flask, render_template
import data_generator as dg
from flask_socketio import send, emit, SocketIO


app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html',data=dg.generator())

@socketio.on('json')
def handle_json(json):
    send(json, json=True)


if __name__ == '__main__':
    print(dg.generator())
    app.run('127.0.0.1',5000,debug=True)

    