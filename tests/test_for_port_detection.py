import serial.tools.list_ports

def find_arduino(serial_number):
    for pinfo in serial.tools.list_ports.comports():
        if pinfo.serial_number == serial_number:
            return serial.Serial(pinfo.device)
    raise IOError("Could not find an arduino - is it plugged in?")

ser = find_arduino(serial_number='85430353531351B09121')