import xmlrpc.client,sys
from datetime import datetime
    
def main():
    global username,data,conn
    print("*"*40)
    ip=input("Ingrese la ip y el puerto del servidor\n")
    print("*"*40)
    try:
        conn = xmlrpc.client.ServerProxy('http://'+ip+'/',allow_none=True)
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
                    file_contents = conn.file_get_contents(file_name)
                    if file_contents == None:
                        print("*"*40)
                        print('404 Archivo no encontrado en nuestros servidores')
                        print("*"*40)
                    else :
                        print("*"*40)
                        print("Contenido de '"+str(file[1])+"'")
                        print("*"*40)
                        print(file_contents)
                        print("*"*40)
            if not found:
                print("*"*40)
                input("No has ingresado ninguna opción correcta...\npulsa una tecla para continuar")
                print("*"*40)
        elif option == '2':
            show_files(data)
            file_to_modify=input("Ingrese el archivo a modificar\n")
            found= False
            for file in data:
                if file_to_modify == str(file[0]):
                    found=True
                    user_id=conn.get_id(username)
                    file_name=str(user_id)+'_'+str(file[0])+'.txt'
                    file_contents = conn.file_get_contents(file_name)
                    if file_contents == None:
                        print("*"*40)
                        print('404 Archivo no encontrado en nuestros servidores')
                        print("*"*40)
                    else :
                        print("*"*40)
                        print("Contenido de '"+str(file[1])+"'")
                        print("*"*40)
                        print(file_contents)
                        print("*"*40)
                        print("Ingrese el nuevo contenido de '"+str(file[1])+"'")
                        print("*"*40)
                        new_file_content = input()
                        print("*"*40)
                        now = datetime.now()
                        status=conn.new_file_content(file_name,new_file_content,file[0],now.strftime("%d")+'/'+now.strftime("%m")+'/'+now.strftime("%Y")+" "+now.strftime("%H:%M:%S"))
                        if status:
                            print('Archivo modificado exitosamente')
                            print("*"*40)
            if not found:
                print("*"*40)
                input("No has ingresado ninguna opción correcta...\npulsa una tecla para continuar")
                print("*"*40)   
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