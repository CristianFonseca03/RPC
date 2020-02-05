import sqlite3

def search_username(username):
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    c.execute("select * from user where name=:name",{"name":username})
    if c.fetchone() != None :
        return True
    else:
        return False
    conn.close()

def get_files(username):
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    c.execute("select id from user where name=:name",{"name":username})
    id = c.fetchone()[0]
    c.execute("select file_id from file_control where user_id=:id",{"id":1})
    data = c.fetchall()
    if len(data) == 0:
        return None
    else:
        user_files = []
        for i in data:
            c.execute("select * from file where id=:id",{"id":i[0]})
            user_files.append(c.fetchone())
        return user_files
    conn.close()

def get_id(username):
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    c.execute("select id from user where name=:name",{"name":username})
    return c.fetchone()[0]
    conn.close()

if __name__=="__main__":
    get_id("Cristian")
    