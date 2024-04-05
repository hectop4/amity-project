from flask import Flask, render_template
from flask_socketio import SocketIO, send


app = Flask(__name__)
app.config['SECRET_KEY'] = 'text'
socketio=SocketIO(app,cors_allowed_origins="*")

@socketio.on('message')
def handle_message(message):
    print('Message: ' + message)
    if message !='User Connected':
        send(message, broadcast=True)



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app,host='10.42.0.230')