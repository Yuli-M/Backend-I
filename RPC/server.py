def add(a, b):
    return a + b
def sub(a,b):
    return a - b

def hi():
    return "Saludo"

from rpc import RPCServer
server = RPCServer('localhost', 8080)
server.registerMethod(add)
server.registerMethod(sub)
server.registerMethod(hi)

server.run()