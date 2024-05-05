import cv2
import mediapipe as mp
from flask import Flask, render_template, Response

# Realizar videocaptura
cap = cv2.VideoCapture(1)
cap1 = cv2.VideoCapture(2)

# Función frame
def frame():
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        else:
            suc, encode = cv2.imencode('.jpg', frame)
            frame = encode.tobytes()
    
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
    # Liberar los recursos de OpenCV
    cap.release()

# Función frame
def frame1():
    while True:
        ret1, frame1 = cap1.read()
        
        if not ret1:
            break
        else:
            suc1, encode1 = cv2.imencode('.jpg', frame1)
            frame1 = encode1.tobytes()
    
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame1 + b'\r\n')
        
    # Liberar los recursos de OpenCV
    cap1.release()


# Crear app
app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta video
@app.route('/video')
def video():
    return Response(frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Ruta video
@app.route('/video1')
def video1():
    return Response(frame1(), mimetype='multipart/x-mixed-replace; boundary=frame')


# Ejecutar aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# Liberar los recursos
cap.release()
cap1.release()