from serial.tools import list_ports
import serial
import sys
import time 


def conn(port):
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = port
    ser.open()
    
    if ser.is_open :
        a = 'c'
        while a !='X':
            line = ser.readline()
            line = line.decode('utf-8')
            print(line)   
            a = input('\nPress X to close the conn or any key to continue: ')
            
        ser.close()   

        print('Connection is Closed !')    
        time.sleep(2)
        print('Thank You!')    




a = list_ports.comports()


#i=0
#print(len(a))

#cur =  str(a[1])
#print(cur)
# if 'CH340' in cur:
#     print('Hello') 

# print(cur[:4])
port = None
if port :
    for i in range(len(a)):
        cur =  str(a[i])
        if 'CH340' in cur:
            print(f'Connecton at found at {cur[:4]}')
            port = cur[:4]
            break
    
    i = input('\nPress S to start reading : ')

    if i =='S':
        conn(port)

else: 
    print("No Connecton Found")