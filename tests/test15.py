import re 
def raw_to_clean():
    line='P10143I+2060E+3438U03711X311234567890'
    regex = '\d+'             
    
    match = re.findall(regex, line) 
    print(match) 

raw_to_clean()    

