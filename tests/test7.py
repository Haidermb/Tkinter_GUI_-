
s1 = ['P', 'I', 'E', 'U', 'X', "t", 'l', 'x', 'o', 'y', 's', 'h']
e1 = ['I', 'E', 'U', 'X', "123456789", 'l', 'x', 'o', 'y', 'q1s', 'h', 'P0']
p1 = ["Pressure", "Int_temp", "Ext_temp", "Humidity", "Voltage", "GPS time",
      "Latitutde", "direction n/s", "Longitude", "direction e/w", "No. of satelite", "GPS altitude"]
len1 = [5, 5, 5, 5, 2, 8, 9, 1, 9, 1, 2, 8]
div = [10, 100, 100, 100, 10, 1, 1, 1, 1, 1, 1, 1]
mylist = []
t = len(s1)
lines = []
raw = 'UUUUUUUU~#+UP10143I+2060E+3438U03711X311234567890'
lines.append(raw)

import re        
regex = r"([P-I]+)"
match = re.search(regex,raw)
#print(match.group())
print(match.group(0))


