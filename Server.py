from xmlrpc.server import SimpleXMLRPCServer
import json

global data

def is_runing():
    return True

def connection(username):
    with open('data.json') as file:
        data = json.load(file)
    try:
        return data[username]
    except KeyError:
        return 1
    
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(is_runing, "is_runing")
server.register_function(connection, "connection")
server.serve_forever()