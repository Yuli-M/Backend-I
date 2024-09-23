import socket
import threading
import sys
import pickle
import os
class Cliente():
    
    def __init__(self, host="localhost", port=7000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(port)))

        msg_recv = threading.Thread(target=self.msg_recv)
        msg_recv.daemon = True 
        msg_recv.start()
        
        while True:
            msg = input('-> ')
            if msg != 'salir':
                self.send_msg(msg)
            else:
                self.sock.close()
                sys.exit()
                
    def msg_recv(self):
        while True:
            try:
                data = self.sock.recv(1028)
                if data:
                    try:
                        data = pickle.loads(data)
                        print(data)
                    except:
                        filename = data.decode().split('/')[-1]
                        if not os.path.exists('download'):
                            os.makedirs('download')
                        filename = os.path.join('download', filename)
                        with open(filename, 'wb') as file:
                            file.write(data)
                        print(f'{filename} guardado en "download"')
            except:
                pass
    
    def send_msg(self, msg): 
        try:
            self.sock.send(pickle.dumps(msg))
        except:
            print('error')

    def get_file(self, filename):
        try:
            self.sock.send(pickle.dumps(f'get {filename}'))
        except:
            print('error')


client = Cliente()
client()