# gestion_usuarios.py
from google.colab import drive

def registro_login(diccionario):
    if not diccionario:
        continuidad = False

        while not continuidad:
            print("\nIngrese 1 para registrarse\nIngrese 2 para loguearse\nIngrese 3 para salir del programa")
            registroLogin = input("Ingrese la acción que desea realizar: ")

            if registroLogin.isdigit():
                registroLogin = int(registroLogin)

                if registroLogin == 1:
                    nombreUsuario = input("\nIngrese un nombre de usuario: ")
                    registrar_usuario(diccionario, nombreUsuario)
                    continuidad = opciones_continuar()
                elif registroLogin == 2:
                    loguear_usuario(diccionario)
                    continuidad = True
                elif registroLogin == 3:
                    print("\nUsted cerró el programa con éxito")
                    continuidad = True
                else:
                    print("\nIngrese un carácter válido")
            else:
                print("\nIngrese un carácter válido\n ")
    else:
        print("Ingrese un diccionario como argumento")

def opciones_continuar():
    print("\nOpciones\n1 Para salir del programa\n2 Para realizar otra acción")
    continuidad1 = False
    while not continuidad1:
        continuar1 = input("Ingrese la acción que desea realizar: ")
        if continuar1.isdigit():
            continuar1 = int(continuar1)
            if continuar1 == 1:
                print("Usted cerró el programa con éxito")
                return True
            elif continuar1 == 2:
                return False
            else:
                print("\nIngrese un carácter válido\n ")
        else:
            print("\nIngrese un carácter válido\n ")

def registrar_usuario(diccionario, nombre_usuario):
    if nombre_usuario in diccionario:
        print("Este nombre de usuario ya está registrado")
    else:
        diccionario[nombre_usuario] = input("Ingrese una contraseña: ")
        print("Registro con éxito")

def loguear_usuario(diccionario):
    nombreUsuario1 = input("Ingrese nombre de usuario: ")
    if nombreUsuario1 in diccionario:
        contraseñaUsuario = input("Ingrese su contraseña: ")
        if diccionario[nombreUsuario1] == contraseñaUsuario:
            print("Usted se ha logueado correctamente")
        else:
            print("Contraseña incorrecta\n")
    else:
        print("Usuario inexistente\n")

def guardar_datos(diccionario):
    if diccionario:
        drive.mount("/drive/", force_remount=True)
        ruta = "/drive/MyDrive/pre-entrega_Damaris_Allue/datos_de_usuario.txt"
        with open(ruta, "a") as f:
            for clave, valor in diccionario.items():
                f.write(f"Usuario: {clave}, Contraseña: {valor}\n")
        print("Datos guardados con éxito.")
    else:
        print("Ingrese un diccionario o no posee ningún dato")

def leer_datos(diccionario):
    try:
        drive.mount("/drive/", force_remount=True)
        ruta = "/drive/MyDrive/pre-entrega_Damaris_Allue/datos_de_usuario.txt"
        with open(ruta, "r") as usuario_contraseña:
            datos = usuario_contraseña.read()
            print(datos)
    except FileNotFoundError:
        print("Error: El archivo de datos no existe. Asegúrate de guardar los datos antes de intentar leerlos.")
    except OSError as e:
        print(f"Error de lectura: {e}")
