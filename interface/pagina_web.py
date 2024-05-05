import cv2
#import mediapipe as mp
from flask import Flask, render_template, Response, request
import serial

#----------------------------- Puerto Serial Configuracion ----------------------------
#com = serial.Serial("COM4", 115200, timeout= 10)
d = 'd' # Derecha
i = 'i' # Izquierda
p = 'p' # Centro
u = 'u' # Arriba
b = 'b' # Abajo

#------------------------------ Declaramos el detector --------------------------------
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#------------------------------ Realizamos VideoCaptura --------------------------------
cap = cv2.VideoCapture(0)
num = 0

# Crear app
app = Flask(__name__)

def frames():
    global frame
    while True:
        # Lectura de fotogramas
        ret, frame = cap.read()
        #  espejo a los frames
        frame = cv2.flip(frame,1)
        txt = 'ROSTRO'

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.rectangle(frame, (x,y-14), (x+65,y), (255,0,0), -1)
            cv2.putText(frame, txt, (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            if x > 300:
                texto = 'derecha'
                l = 70
                #com.write(d.encode('ascii'))
            elif x < 190:
                texto = 'izquierda'
                l = 77
                #com.write(i.encode('ascii'))
            elif y < 120:
                texto = 'arriba'
                l = 50
                #com.write(u.encode('ascii'))
            elif y > 170:
                texto = 'abajo'
                l = 45
                #com.write(b.encode('ascii'))
            else:
                texto = 'centro'
                l = 57
                #com.write(p.encode('ascii'))
            cv2.rectangle(frame, (0,0), (l,14), (255,0,0), -1)
            cv2.putText(frame, texto, (0,13), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1)
        
        if not ret:
            break
        else:
            suc, encode = cv2.imencode('.jpg', frame)
            frame = encode.tobytes()
        
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
    # Liberar los recursos
    cap.release()
    cv2.destroyAllWindows()

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta video
@app.route('/video')
def video():
    return Response(frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Ejecutar aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
