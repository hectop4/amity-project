from flask import Flask, render_template, url_for, request, redirect, make_response, Response
import random
import json
from time import time
from random import random
import data_generator as dg
from flask_socketio import send, emit, SocketIO
import serial_reader as sr
import serial_writer as sw
from camera import Camera

app = Flask(__name__)
socketio = SocketIO(app)
camera = Camera()



@app.route('/' , methods=['GET', 'POST'])
def main():
    return render_template('index.html', data=dg.generator())

@app.route('/data', methods=['GET', 'POST'])
def data():
    try:
        data=[time() * 1000,  float(sr.data_to_dict(sr.read_serial())["T2"])]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
        return response
    except:
        return "Error"

@app.route('/action', methods=['POST'])        
def handle_action():
    data = request.json
    if data['key'] == 'f':
        # Realizar la acción correspondiente en el controlador
        print('Se recibió la letra "f" desde el cliente.')
        sw.write_serial('f')
        # Devolver una respuesta al cliente si es necesario
        return 'Acción recibida exitosamente', 200
    
    elif data['key'] == 'l':
        # Realizar la acción correspondiente en el controlador
        print('Se recibió la letra "l" desde el cliente.')
        sw.write_serial('l')
        # Devolver una respuesta al cliente si es necesario
        return 'Acción recibida exitosamente', 200
    elif data['key'] == 'r':
        # Realizar la acción correspondiente en el controlador
        print('Se recibió la letra "r" desde el cliente.')
        sw.write_serial('r')
        # Devolver una respuesta al cliente si es necesario
        return 'Acción recibida exitosamente', 200
    elif data['key'] == 'b':
        # Realizar la acción correspondiente en el controlador
        print('Se recibió la letra "b" desde el cliente.')
        sw.write_serial('b')
        # Devolver una respuesta al cliente si es necesario
        return 'Acción recibida exitosamente', 200
    elif data['key'] == 's':
        # Realizar la acción correspondiente en el controlador
        print('Se recibió la letra "s" desde el cliente.')
        sw.write_serial(' ')
        # Devolver una respuesta al cliente si es necesario
        return 'Acción recibida exitosamente', 200
    elif data['key'] == 'z':
        # Realizar la acción correspondiente en el controlador
        print('Se recibió la letra "z" desde el cliente.')
        sw.write_serial('c')
        # Devolver una respuesta al cliente si es necesario
        return 'Acción recibida exitosamente', 200
    elif data['key'] == 'x':
        # Realizar la acción correspondiente en el controlador
        print('Se recibió la letra "x" desde el cliente.')
        sw.write_serial('d')
        # Devolver una respuesta al cliente si es necesario
        return 'Acción recibida exitosamente', 200
    else:
        return 'Error: Clave incorrecta', 400
    
def generate_frames():
    while True:
        frame = camera.get_frame()
        if frame is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    print(dg.generator())

    print(sr.read_serial())
    app.run(host='0.0.0.0',port=5500,threaded=True,debug=True)

    