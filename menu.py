import random
import json

# # Cargar datos en un archivo JSON
# archivo = open("configuracion.json", "r")
# datos = json.load(archivo) #diccionario
# archivo.close()
# print(type(datos))
# print(datos)

# # Guardar una estructura de datos en python
# datos = {
#     "usuario": "root",
#     "modo_oscuro": False,
#     "idiomas": ["es"]
# }

# archivo = open("configuracion.json", "a")
# json.dump(datos, archivo, indent=4)
# archivo.close()


nombre_usuario = input("Ingrese su nombre: ")
mensaje_error = f"Intente nuevamente {nombre_usuario}"
mensaje_menu = "Seleccione la opción: \n\n[1] Jugar \n[2] Puntajes \n[3] Salir \n"
mensaje_menu += f"\n\nSELECCIONE OPCIÓN {nombre_usuario}: "

while True:
    menu = int(input(mensaje_menu))

    match menu:
        case 1:
            try:
                user_input = input(f"{nombre_usuario}, seleccione Es/En: ").upper
                
            except:
                print(mensaje_error)
        case 2:
            pass    
        case 3:
            break