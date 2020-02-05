from xmlrpc.server import SimpleXMLRPCServer
import db

def is_runing():
    return True

def user_exists(username):
    return db.search_username(username)

def get_user_files(username):
    return db.get_files(username)

def get_id(username):
    return db.get_id(username)

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(is_runing, "is_runing")
server.register_function(user_exists, "user_exists")
server.register_function(get_user_files, "get_user_files")
server.register_function(get_id, "get_id")
server.serve_forever()