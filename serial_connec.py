import serial
from serial.tools import list_ports


class SerialConnection():

    def __init__(self) -> None:
        
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
