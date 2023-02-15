import serial
ser = serial.Serial()
ser.baudrate = 19200
ser.port = 'COM8'
#print(ser)
# ser.open() NOT REQUIRED IF PORT IS ALREADY SPECIFY 
# But her it is actually requred as ser.port is specified after initialization
# but see ser1 it is already open as port is specified during initialization 
print(ser.is_open)
print(ser.port)

ser1 = serial.Serial(
    port='COM3',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser1.portstr)

count=1


while True:
    for line in ser1.read_all():

        print(str(count) + str(': ') + chr(line) )
        count = count+1


ser1.close()


available = list_ports.comports()