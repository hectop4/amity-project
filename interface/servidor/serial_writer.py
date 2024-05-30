import serial

# Configure the serial port
ser = serial.Serial('/dev/ttyACM1', 115200)  # Replace '/dev/ttyUSB0' with your serial port

def write_serial(data):
    # Write data to the serial monitor
    ser.write(data.encode())