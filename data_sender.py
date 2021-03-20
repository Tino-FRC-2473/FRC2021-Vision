import serial

class DataSender:

    def __init__(self, name="ttyS0", rate=9600):
        self.s = serial.Serial('/dev/'+name, rate)

    def send_data(self, pattern):
        data_to_send = pattern
        print(data_to_send)
        self.s.write(bytes("S " + data_to_send + " E", 'utf-8'))  # S is start, E is end. AR is Path A Red, etc
