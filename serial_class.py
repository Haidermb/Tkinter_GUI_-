import serial 
from serial.tools import list_ports
import keyboard
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random



def find_data(line):
     
    s1 = ['P', 'I', 'E', 'U', 'X', "t", 'l', 'x', 'o', 'y', 's', 'h']
    e1 = ['I', 'E', 'U', 'X', "123456789", 'l', 'x', 'o', 'y', 'q1s', 'h', 'P0']
    p1 = ["Pressure", "Int_temp", "Ext_temp", "Humidity", "Voltage", "GPS time",
      "Latitutde", "direction n/s", "Longitude", "direction e/w", "No. of satelite", "GPS altitude"]
    len1 = [5, 5, 5, 5, 2, 8, 9, 1, 9, 1, 2, 8]
    div = [10, 100, 100, 100, 10, 1, 1, 1, 1, 1, 1, 1]
    mylist = []

    line = line

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



class SerialConnection():


    

    def __init__(self) -> None:

        
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.xs = []
        self.ys = []
        
        
        self.__port=None
        self.__baudrate=9600
        self.__parity=serial.PARITY_NONE
        self.__stopbits=serial.STOPBITS_ONE
        self.__bytesize=serial.EIGHTBITS
        self.__timeout=1

        self.__Serial = serial.Serial(port=self.__port, baudrate=self.__baudrate, parity=self.__parity, stopbits=self.__stopbits, bytesize=self.__bytesize, timeout=self.__timeout )

    def __str__(self) -> str:
        return f'{self.__Serial}'
    
    
    def set_port(self,port):
        '''
        use to set port for conn 
        return None 
        '''
        self.__Serial.port = port
        print(f'connected to {self.__Serial.portstr}')
        
    def get_port (self):
        '''
        Return curr connected port 
        '''
        port  = self.__Serial.port
        return port 

    def check_activite_conn(self):

        avai =  list_ports.comports() 
        for i in range(len(avai)):
            cur =  str(avai[i])
            if 'CH340' in cur:
                a = cur[:4]
                return a 

    
    def get_all_ports(self):
        '''
        Returns a dictionary containg all avaialable ports  
        Input : None 
        Output : A dict {key->int : value->str}
               : if ports are not available it return False -> bool
        '''
        avai =  list_ports.comports() 
        
        if len(avai) > 0:
            new_port = []
            new_name= []
            for i in range(len(avai)):
                cur_port =  str(avai[i])
                port = cur_port[:4]
                name = cur_port[6:]
                new_port.append(port)
                new_name.append(name)

            l = [i for i in range (1,len(avai)+1)]
        
            avai_port_dict = {}
            avai_name_dict ={}
            for i , port in zip(l,new_port):
                avai_port_dict.update({i:port})

            for i , name in zip(l,new_name):
                avai_name_dict.update({i:name})

        # yield avai_port_dict        
        # yield avai_name_dict

        return [avai_port_dict,avai_name_dict]            
    
    def __start_conn (self):
        '''
        Start the serial conn with current port specified
        Returns a Boolean Value True if conn is open else False   
        '''
        self.__Serial.open()
        res = self.__Serial.is_open
        return res

    def __close_conn(self):
        '''
        Close the serial conn 
        Returns a Boolean Value False if conn is Closed 
        else True if conn is open
        '''

        self.__Serial.close()
        
        return self.__Serial.is_open
 
    def __read_data(self):

        """Read data line by line and return it """

        line = self.__Serial.readline()
        line = line.decode('utf-8')
        return line

    def __user_input(self):
        para = ['Pressure','Int_temp','Ext_temp','Humidity','Voltage']    
        l = [i for i in para]
        
    def c_animate(self,i, xs, ys):


        line = self.__read_data() 
        dict_value  = find_data(line[12:])
        if dict_value :
                
            p = dict_value['Pressure']
            it = dict_value['Int_temp']
            et = dict_value['Ext_temp']
            h = dict_value['Humidity']
            v = dict_value['Voltage']
        


        # Add x and y to lists
        xs.append(dt.datetime.now().strftime('%H:%M:%S'))
        ys.append(h)

        # Limit x and y lists to 20 items
        xs = xs[-20:]
        ys = ys[-20:]

        # Draw x and y lists
        self.ax.clear()
        self.ax.plot(xs, ys)

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('TMP102 Temperature over Time')
        plt.ylabel('Temperature (deg C)')

    def start_graph(self):

        ani = animation.FuncAnimation(self.fig, self.c_animate, fargs=(self.xs, self.ys), interval=1000)
        plt.show()

    def find_data(self,line):
        
        s1 = ['P', 'I', 'E', 'U', 'X', "t", 'l', 'x', 'o', 'y', 's', 'h']
        e1 = ['I', 'E', 'U', 'X', "123456789", 'l', 'x', 'o', 'y', 'q1s', 'h', 'P0']
        p1 = ["Pressure", "Int_temp", "Ext_temp", "Humidity", "Voltage", "GPS time",
        "Latitutde", "direction n/s", "Longitude", "direction e/w", "No. of satelite", "GPS altitude"]
        len1 = [5, 5, 5, 5, 2, 8, 9, 1, 9, 1, 2, 8]
        div = [10, 100, 100, 100, 10, 1, 1, 1, 1, 1, 1, 1]
        mylist = []

        line = line

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

    def main(self):



        try :     
            all = self.get_all_ports()
            if all != False:
                ports = all[0]
                names = all[1]
                for k,v in zip(names.keys(),names.values()):
                    print(f'{k}) {v}')
                try:
                    i = None
                    i = int(input('Select any Port Press respective Number (1-9) : '))
                    if type(i) != int:
                       i = int(i)           
                except :
                    print('input should be integer only (1-9)')
                
                if (type(i) == int) and (i in range (1,10)):
                    port = None
                    port = ports.get(i)

                    if port :
                        self.set_port(port)

                        try : 
                            a = self.__start_conn()
                            if a:
                                self.start_graph()
                                    
                                while self.__Serial.is_open: 
                                    line = self.__read_data()
                                    #print(line[11:])
                                    dict_value  = find_data(line[12:])
                                    #print(dict_value)
                                    if dict_value:
                                        res = self.__close_conn()
                                    if keyboard.is_pressed('q'):
                                        res = self.__close_conn()

                                res = self.__close_conn()        

                                p = dict_value['Pressure']
                                it = dict_value['Int_temp']
                                et = dict_value['Ext_temp']
                                h = dict_value['Humidity']
                                v = dict_value['Voltage']

                                print(f'\nPressure : {p}\nInternal_temp : {it}\nExternal_temp : {et}\nHumidity : {h}\nVoltage : {v}\n')

                                if dict_value:
                                    try: 
                                        p_u = float(input('\nEnter Presure : '))
                                        it_u = float(input('\nEnter Internal_temp : '))
                                        et_u = float(input('\nEnter External_temp : '))
                                        h_u = float(input('\nEnter Humidity : '))
                                        v_u = float(input('\nEnter Voltage : '))
                                    except:
                                        print('User Input Error')  

                                    er_p = p_u-p
                                    er_it = it_u-it
                                    er_et = et_u-et
                                    er_h = h_u-h
                                    er_v = v_u-v       

                                    print(f'\n2Error in Pressure : {abs(er_p)}\nError in Internal_temp : {abs(er_it)}\nError in External_temp : {abs(er_et)}\nError in Humidity : {abs(er_h)}\nError in Voltage : {abs(er_v)}\n')
 

                                if res == False:
                                    print('Connection is Closed')

                        except ValueError: 
                    
                            print(f'Error in starting connection to port {port}')        

                    else : 
                        print('Invalid Port Selected')
                else :
                    print('Error in user input')
            else:
                print('No Ports available')
        except ValueError:
            print('test')
    

if __name__ == '__main__':
    
    ser = SerialConnection()
    
    ser.main()