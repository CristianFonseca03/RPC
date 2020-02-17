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
    user_id = get_id(username)
    c.execute("select file_id from file_control where user_id=:id",{"id":user_id})
    data = c.fetchall()
    if data == None:
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

def change_modify_date(id,date):
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    c.execute("update file set modification_date=:date where id=:id",{"date":date,"id":id})
    conn.commit()
    conn.close()


    