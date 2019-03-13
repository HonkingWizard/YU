import serial 
import threading
import requests
import time

class DeviceHandler:
    
    def __init__(self,baud_rate = 9600,serial_port = '/dev/ttyUSB0',server_address = 'http://127.0.0.1:3000/post-data'):
        self.baud_rate = baud_rate
        self.serial_port = serial_port
        self.server_address = server_address 

        try:
            self.uc = serial.Serial(self.serial_port,self.baud_rate)

        except:
            print("\nPermission issues detected while accessing the port.\n\tTry running - 'sudo chmod a+rw /dev/ttyUSB0'\n")
            exit()

    def run(self):
        try:
            FetchedData = self.uc.readline()
            FetchedData = FetchedData.decode("utf-8") 
        except:
            print('\nHaving issues with decoding...')
            return

        data ={
            'SensorValue': FetchedData
        }

        r = requests.post(self.server_address,data)
        print('\n\tValue Sent -> ' + str(data['SensorValue']) )         



if __name__ == "__main__":
    
    handler = DeviceHandler()
    
    while True:
        handler.run()
        time.sleep(10)
