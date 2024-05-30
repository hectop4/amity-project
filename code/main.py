import cv2
import serial

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
ser = serial.Serial('/dev/ttyACM0', 115200)
# Initialize the video capture
cap = cv2.VideoCapture(0)


def data_writer(data):
    ser.write(data.encode())

while True:
    # Read the frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frameqq
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        if x < 200:
            print('izquierda')
            data_writer('c')
        elif x > 400:   
            print('derecha')
            data_writer('d')
        

    # Display the frame
    cv2.imshow('Face Detection', frame)

    

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()