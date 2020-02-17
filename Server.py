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

def file_get_contents(file_name):
    try:
        with open('files/'+file_name) as f:
            return f.read()
    except FileNotFoundError:
        return None

def new_file_content(file_name,new_content,id,date):
    with open('files/'+file_name,'w') as f:
        f.write(new_content)
        db.change_modify_date(id,date)
    return True


server = SimpleXMLRPCServer(("0.0.0.0", 8000), allow_none=True)
print("Listening on port 8000...")
server.register_function(is_runing, "is_runing")
server.register_function(user_exists, "user_exists")
server.register_function(get_user_files, "get_user_files")
server.register_function(get_id, "get_id")
server.register_function(file_get_contents, "file_get_contents")
server.register_function(new_file_content, "new_file_content")
server.serve_forever()