import serial 
from serial.tools import list_ports


class Connect():
    
    def __init__(self) -> None:
        
        
        self.__port=None
        self.__baudrate=9600
        self.__parity=serial.PARITY_NONE
        self.__stopbits=serial.STOPBITS_ONE
        self.__bytesize=serial.EIGHTBITS
        self.__timeout=0

        self.__Serial = serial.Serial(port=self.__port, baudrate=self.__baudrate, parity=self.__parity, stopbits=self.__stopbits, bytesize=self.__bytesize, timeout=self.__timeout )

    def __str__(self) -> str:
        return f'{self.Serial}'
    
    
    def __connect(self,port):

        self.port = port     
        self.__Serial.port = self.port
        print(f"connected to:  {self.__Serial.portstr}")
        self.__start_conn()
        self.__read_data()
    
    def change_port(self,port):

        self.__connect(port) 

    def check_activite_conn(self):

        avai =  list_ports.comports() 
        for i in range(len(avai)):
            cur =  str(avai[i])
            if 'CH340' in cur:
                #print(f'Connecton at found at {cur[:4]}')
                a = cur[:4]
                self.__port = a
                return 

    def __start_conn (self):
        self.__Serial.open()

    def __closed_conn(self):
        self.__Serial.close()

    def __read_data(self):

        """Read data and return it""" 
        line = self.__Serial.readline()
        line = line.decode('utf-8')
        return line
                  


a = Connect()



#print(a)
a.change_port('COM3')


available = list_ports.comports()
