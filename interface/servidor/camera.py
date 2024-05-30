import cv2

class Camera:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)  # Inicia la captura de video desde la cámara


    def get_frame(self):
        success, frame = self.camera.read()  # Lee un frame de la cámara
        if not success:
            return None
        else:
            ret, buffer = cv2.imencode('.jpg', frame)  # Codifica el frame en formato JPEG
            frame_bytes = buffer.tobytes()  # Convierte el frame en bytes
            return frame_bytes

    def release(self):
        self.camera.release()  # Libera los recursos de la cámara

