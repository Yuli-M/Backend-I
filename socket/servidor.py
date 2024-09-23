import socket
import threading
import sys
import pickle
#from os import listdir, path
import os
class Servidor():
    
    def __init__(self, host="localhost", port=7000):
        #arreglo para guardar los clientes conectados
        self.clientes = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((str(host), int(port)))
        self.sock.listen(10)
        self.sock.setblocking(False)
        
        #hilos para aceptar y procesar las conexiones
        aceptar = threading.Thread(target=self.aceptarCon)
        procesar = threading.Thread(target=self.procesarCon)
        
        aceptar.daemon = True 
        aceptar.start()
        procesar.daemon = True 
        procesar.start()
        
        try:
            while True:
                msg = input('-> ')
                if msg == 'salir':
                    break
            self.sock.close()
            sys.exit()
        except:
            self.sock.close()
            sys.exit()

     # envia el mensaje a todos los clientes excepto al que lo envio     
    def msg_to_all(self, msg, cliente):
        for c in self.clientes:
            try:
                if c != cliente:c.send(msg)
            except:
                self.clientes.remove(c)
    
    def aceptarCon(self):
        print("aceptarCon iniciado")
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                self.clientes.append(conn)
            except:
                pass
            
    def procesarCon(self):
        print("ProcesarCon iniciado") 
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c.recv(1024)
                        if data:
                            msg = pickle.loads(data)

                            if msg.startswith('ls'):
                                self.comando_ls(msg, c)
                            elif msg.startswith('get'):
                                self.comando_get(msg, c)
                            else:
                                self.msg_to_all(data,c)
                    except:
                        pass

    def comando_ls(self, msg, cliente):
        partes = msg.split()# espacios

        if len(partes) == 0:
            return
        comando = partes[0] #el comando es la primera parte

        if comando == 'ls':
            if len(partes) > 1:
                directorio = partes[1]
            else:
                directorio = '.'

            if os.path.isdir(directorio):
                lista = os.listdir(directorio)
                respuesta = f"{directorio}" + "\n".join(lista)
            else:
                respuesta = f"{directorio} no encontrado"

            cliente.send(pickle.dumps(respuesta))
        else:
            respuesta = f"{comando} no se reconoce"
            cliente.send(pickle.dumps(respuesta))

    def comando_get(self, msg, cliente):
        partes = msg.split()
        if len(partes) < 2:
            respuesta = "Comando: get <nombre_archivo>"
            cliente.send(pickle.dumps(respuesta))
            return
        
        filename = partes[1]
        files = '/home/yuli/Documents/workspace/back/socket/files'
        filename = os.path.join(files, filename)

        if os.path.isfile(filename):
            with open(filename, 'rb') as file: #rb modo binario
                contenido = file.read()
                cliente.send(contenido)

        else:
            respuesta = f"{filename} no encontrado"
            cliente.send(pickle.dumps(respuesta))
        
        
    
    #def ls(ruta = '/Documents/workspace/back/files'):
        #return listdir(ruta)

server = Servidor()
server()