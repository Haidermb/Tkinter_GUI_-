from serial.tools import list_ports
import sys
import time 
a = list_ports.comports()

# for i in a:
#     print(i)

i=0
#print(a[0])
print(len(a))
while i < len(a):
    if "CH340" in a[i]:
        str2 = str(i)
        str1 = "COM" + str2

    if "CH340" in a[i] and str1 in a[i]:
        print ("Found Arduino Uno on " + str1)
        break    

    if i == len(a):

        print('Ardino Not Found')
        sys.exit()    

    
    i += 1

print('end')    
time.sleep(5)            