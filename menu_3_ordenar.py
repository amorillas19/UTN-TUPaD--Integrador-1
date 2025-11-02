import os
from operator import itemgetter
from colorama import Fore, Back, Style, init
init(autoreset=True)

#Sirve para pedir al usuario una opcion para ordenar los paises, en base a eso crea una entrada para
#la funcion revertir()

def ordenar_paises (lista_paises):

    while True:

        print(Back.LIGHTGREEN_EX + Fore.BLACK + "Opcion 3")
        print ("")
        print(Back.LIGHTGREEN_EX + Fore.BLACK + "======== ORDENAR PAISES ========")
        print(Back.LIGHTWHITE_EX + Fore.BLACK +"""  [1] Ordenar por nombre          
        [2] Ordenar por poblacion       
        [3] Ordenar por superficie
        [4] Volver al menu principal      """)
        print(Back.LIGHTGREEN_EX + Fore.BLACK + "================================")

        menu_ordenar = input(Back.LIGHTWHITE_EX + Fore.BLACK + "Que opcion desea realizar: ")
        print("")
        os.system('cls')

        match menu_ordenar:
            case "1":
                ordenar(lista_paises, "nombre")

            case "2":
                ordenar(lista_paises, "poblacion")

            case "3":
                ordenar(lista_paises, "superficie")

            case "4":
                break

            case _:
                print("Opcion no valida")


#Sirve para preguntar al usuario por el orden en el que se va a organizar la lista y en base a eso llamar
#a la funcion ordena()

def ordenar (lista_paises, itemgetter:str):

    while True:
        print (Back.LIGHTWHITE_EX + Fore.BLACK + """
        [1] Ascendete (A-Z)  
        [2] Descendente (Z-A)
        [3] Volver al menu de Ordenar Paises""")
        print("")
        respuesta = input (Back.LIGHTBLACK_EX + Fore.BLACK +"        Desea ordenar de forma asccendente o descendente: ")
        print("")
        os.system('cls')

        match respuesta:

            case "1":
                ordenar_andres_a_to_z(lista_paises, itemgetter)

            case "2":
                ordenar_andres_z_to_a(lista_paises, itemgetter)

            case "3":
                break

            case _:
                print("Opcion no valida")



#Sirve para ordenar la lista en base a los parametros ingresados por el usuario, ademas permite ordenar la
#lista en orden inverso 

def ordenar_andres_a_to_z(lista_paises:list, parametro:str):

    az = sorted(lista_paises, key=itemgetter(parametro))
    print(Back.LIGHTGREEN_EX + Fore.BLACK +"""
============================================ LISTA ORDENADA A-Z ============================================""")
    for i in range(len(az)):
        print(f"""Nombre: {az[i]["nombre"]}  Poblacion: {az[i]["poblacion"]}  Superficie: {az[i]["superficie"]}  Continente: {az[i]["continente"]}""")
        print("--------------------------------------------------------")
    print("=============== FIN DE LISTA ===============")
    pausar_menu = input("Pulse una tecla para continuar: ")
    os.system('cls')
    

def ordenar_andres_z_to_a(lista_paises:list, parametro:str):

    za = sorted(lista_paises, key=itemgetter(parametro), reverse=True)
    print(Back.LIGHTGREEN_EX + Fore.BLACK +"""
============================================ LISTA ORDENADA Z-A ============================================""")
    for i in range(len(za)):
        print(f"""Nombre: {za[i]["nombre"]}  Poblacion: {za[i]["poblacion"]}  Superficie: {za[i]["superficie"]}  Continente: {za[i]["continente"]}""")
        print("--------------------------------------------------------")
    pausar_menu = input("Pulse una tecla para continuar: ")
    os.system('cls')

