import xmlrpc.client
import json,sys

global data

ip=""
username=""
data=""

def show_files(data):
    print("Seleccione un archivo")
    i = 1
    for p in data['files']:
        print(str(i)+") "+p['name'])
        i += 1
    try:
        file = int(input())
    except:
        print("*"*40)
        print("Ingrese a un valor numerico")
        print("*"*40)
        show_files(data)
    else:
        if file > 0 and file <= (i-1) :
            # TODO
        else:
            print("*"*40)
            print("Ingrese a un numero valido")
            print("*"*40)
            show_files(data)

def main():
    print("*"*40)
    ip=input("Ingrese la ip y el puerto del servidor\n")
    print("*"*40)
    username=input("Ingrese el nombre del usuario\n")
    print("*"*40)
    try:
        rpc_server = xmlrpc.client.ServerProxy("http://"+ip+"/")
        rpc_server.is_runing()
    except:
        print("Error al establecer conexión con el servidor")
        sys.exit(1)
    else:
        data = rpc_server.connection(username)
        if  data == 1:
            print("Username no encontrado")
            sys.exit(1)
        else:
            show_files(data)
            
        
    



if __name__=="__main__":
    main()