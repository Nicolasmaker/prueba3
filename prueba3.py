import json
import os

biblioteca = 'biblioteca.json'

with open(biblioteca, "r") as archivos:
    datos = json.load(archivos)
    

#MENU
def main_menu():
    print("*******************************")
    print("         MUNDO LIBRO")
    print("*******************************")

    print("[1]-Mantenedor de autores")
    print("[2]-Reportes")
    print("[3]-Salir")

def menu_mantenedor():
    print("****************************************")
    print(           "MANTENEDOR AUTORES           ")
    print("****************************************")
    print("[1]- Agregar autor")
    print("[2]- Editar autor")
    print("[3]- Eliminar autor")
    print("[4]- Buscar autor")
    print("[6]- Volver")

    
def agregar_autor():
    autorID = int(input("Ingresa IDautor:" ))
    nombre = input("Ingresa Nombre: ")
    nacionalidad = input("Ingresa nacionalidad: ")

    agregar_dato ={
        "AutorID": autorID, 
        "Nombre": nombre,
        "Nacionalidad": nacionalidad
    }

    datos.append(agregar_dato)

    with open(biblioteca, "w") as archivos:
        json.dump(datos["Autor"],archivos)

def editar_autor():
    with open(biblioteca, "r") as archivos:
        datos = json.load(archivos)
    ID = input("Ingresa ID de el autor: ")

    for id in datos:
        if ID == id:
            print("Autor encontrado")
        else:
            print("Autor no encontrado")

def eliminar_autor():
    with open(biblioteca, "r") as archivos:
        datos = json.load(archivos)

        ID =  input("Ingrese ID de el autor: ")

        
        eliminar_datos ={
            "AutorID": ID, 
            
        }

        datos.delete(eliminar_datos)

def buscar_datos():
    with open(biblioteca, "r") as archivos:
        datos = json.load(archivos)
        print(datos)

main_menu()
opc = int(input("Ingrese una opcion: "))

if opc == 1:
    menu_mantenedor
    if opc == 1:
        agregar_autor()
    elif opc == 2:
        editar_autor()
    elif opc == 3:
        eliminar_autor()
    elif opc == 4:
        buscar_datos
    elif opc == 5:
        main_menu
        



