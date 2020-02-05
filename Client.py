import xmlrpc.client,sys
    
def main():
    global username,data,conn
    print("*"*40)
    ip=input("Ingrese la ip y el puerto del servidor\n")
    print("*"*40)
    try:
        conn = xmlrpc.client.ServerProxy("http://"+ip+"/")
        conn.is_runing()
    except:
        print("Error al establecer conexión con el servidor")
        sys.exit(1)
    print("Conexión establecida")
    print("*"*40)
    username=input("Ingrese el nombre del usuario\n")
    if conn.user_exists(username):
        data= conn.get_user_files(username)
        menu()
    else:
        print("*"*40)
        print("Usuario no encontrado")
        sys.exit(1)
        
def menu():
    show_files(data)
    while True:
        print("Seleccione una opción\n1) Leer archivo\n2) Modificar archivo\n3) Salir")
        option = input()
        if option == '1':
            show_files(data)
            file_to_read=input("Ingrese el archivo a leer\n")
            found= False
            for file in data:
                if file_to_read == str(file[0]):
                    found=True
                    user_id=conn.get_id(username)
                    file_name=str(user_id)+'_'+str(file[0])+'.txt'
                    try:
                        file_reader = open('files/'+file_name,'r')
                        print("*"*40)
                        print(file[1])
                        print("*"*40)
                        print (file_reader.read())
                        print("*"*40)
                        file_reader.close()
                    except FileNotFoundError:
                        print("*"*40)
                        print('404 Archivo no encontrado en nuestros servidores')
                        print("*"*40)
            if not found:
                print("*"*40)
                input("No has ingresado ninguna opción correcta...\npulsa una tecla para continuar")
                print("*"*40)
        elif option == '2':
            pass
            #TODO
        elif option == '3':
            break
        else:
            print("*"*40)
            input("No has ingresado ninguna opción correcta...\npulsa una tecla para continuar")
            print("*"*40)

def show_files(file_data):
    if len(file_data) == 0:
        print("*"*40)
        print('El usuario no tiene archivos creados')
        print("*"*40)
        sys.exit(1)
    else:
        print("*"*40)
        for file in file_data:
            print(str(file[0])+') '+file[1]+'\n   Creación: '+file[2]+'\n   Última modificación: '+file[3]+'\n   Creado por: '+username)
        print("*"*40)

if __name__=="__main__":
    main()