# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
contador = 0
while contador < 2:

    archivo = open("login.txt","r")
    nombre=input("\nIngrese su nombre de usuario: ")
    if nombre==archivo.read():
        print("usuario correcto")
        archivo2 = open("clave.txt","r")
        contra=input("\nIngrese su contraseña: ")
        if contra==archivo2.read():
            contador = 3     
            print("\nDatos Producto")
            print("1.Listar")
            print("2.Agregar")
            print("3.Salir")
        else:
            print("contraseña incorrecta")
        archivo2.close()
    else:
        print("Nombre de usuario incorrecto")
    archivo.close()

    contador += 1
    