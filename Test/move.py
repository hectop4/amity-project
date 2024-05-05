import serial
import getch


# Connect to the serial monitor
ser = serial.Serial('/dev/ttyUSB0', 115200)  # Replace '/dev/ttyUSB0' with your serial port

while True:
    key = getch.getch()

    if key == 'w':
        ser.write(b'f')  # Write 'f' to the serial monitor
    elif key == 'a':
        ser.write(b'l')  # Write 'l' to the serial monitor
    elif key == 's':
        ser.write(b'b')  # Write 'b' to the serial monitor
    elif key == 'd':
        ser.write(b'r')  # Write 'r' to the serial monitor
    elif key == 'o':
        ser.write(b'o')
    else:
        ser.write(b's')  # Write 's' to the serial monitor when no key is pressedx  