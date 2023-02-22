import serial

ser = serial.Serial()
ser.port = 'COM8'
ser.open()
#print(ser.is_open)
#ser.close()test
#print(ser.is_open)
ser.timeout = 1
ser.close()


