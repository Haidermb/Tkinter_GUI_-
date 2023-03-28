import re 
def raw_to_clean():
    line='P10143I+2060E+3438U03711X311234567890'
    regex = '\d+'             
    
    match = re.findall(regex, line) 
    print(match) 

raw_to_clean()    

def find_data(line):
     
    s1 = ['P', 'I', 'E', 'U', 'X', "t", 'l', 'x', 'o', 'y', 's', 'h']
    e1 = ['I', 'E', 'U', 'X', "123456789", 'l', 'x', 'o', 'y', 'q1s', 'h', 'P0']
    p1 = ["Pressure", "Int_temp", "Ext_temp", "Humidity", "Voltage", "GPS time",
      "Latitutde", "direction n/s", "Longitude", "direction e/w", "No. of satelite", "GPS altitude"]
    len1 = [5, 5, 5, 5, 2, 8, 9, 1, 9, 1, 2, 8]
    div = [10, 100, 100, 100, 10, 1, 1, 1, 1, 1, 1, 1]
    mylist = []

    line = line
    line='P10143I+2060E+3438U03711X311234567890'

    output = {}
    for i in range(len(s1)):
        beg = line.find(s1[i])
        end = line.find(e1[i])
        if beg == -1 or end == -1:
            continue
        val = line[beg+1:end]
        if len(val) <= len1[i]:
            try:

                value = int(val)/div[i]
                output[p1[i]] = value
            except:
                try:
                    value = val
                    output[p1[i]] = value
                except:
                    continue
        else:
            continue
    #mylist.append(output)
    return output

