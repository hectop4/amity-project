import serial

# Configure the serial port
ser = serial.Serial('/dev/ttyUSB0', 115200)  # Replace '/dev/ttyUSB0' with your serial port

def read_serial():
    # Read data from the serial monitor
    data = ser.readline().decode().strip()
    return data



def data_to_dict(data):
    # Convert the data to a dictionary
    splited={}
    for i in data.split(","):
        try:
            splited[i.split(":")[0]]=i.split(":")[1]
            

        except IndexError:  
            pass
    return splited

def main():
    while True:
        data = read_serial()
        data_dict = data_to_dict(data)
        print(data_dict)

if __name__ == '__main__':
    main()