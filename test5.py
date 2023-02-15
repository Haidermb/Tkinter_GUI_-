a ={1 :'h',
    2:'a',
    3:'i'

}


b = 'hai'
b = list(b)
#print(b)
#c = {i:b.value}
#print(b.value)
l = [i for i in range (1,len(b)+1)]
print(l)
#for i in a.values():
#    print(i)
dic = {
}
for i , v in zip(l,b):
    dic.update({i:v})


for k,v in zip(dic.keys(),dic.values()):
    print(f'{k}) {v}')

input = int(input('Select any Port Press respective Number (1-9) : '))

if (type(input) == int) and (input in range (1,10)):
    
    #print(input)
    port = None
    port = dic.get(input)
    #print(v)    

    if port !=None :
        self.


