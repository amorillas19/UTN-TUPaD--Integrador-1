import os
from operator import itemgetter
from f_validaciones import validar_minimo_maximo
from f_varias import normalizar_pais
from colorama import Fore, Back, Style, init
init(autoreset=True)

#Sirve para ordenar la lista en base a los parametros ingresados por el usuario, ademas permite ordenar la
#lista en orden inverso 

def ordenar_andres_a_to_z(lista_paises:list, parametro:str):

    az = sorted(lista_paises, key=itemgetter(parametro))
    print(Back.LIGHTGREEN_EX + Fore.BLACK +"""
============================================ LISTA ORDENADA: ASCENDIENTE ============================================""")
    for i in range(len(az)):
        print(f"""Nombre: {az[i]["nombre"].capitalize()}  Poblacion: {az[i]["poblacion"]}  Superficie: {az[i]["superficie"]}km2 Continente: {az[i]["continente"].capitalize()}""")
        print(Fore.BLACK + "--------------------------------------------------------")
    print(Back.LIGHTGREEN_EX + Fore.BLACK +"=============== FIN DE LISTA ===============")
    pausar_menu = input("Pulse ENTER para continuar: ")
    os.system('cls')
    

def ordenar_andres_z_to_a(lista_paises:list, parametro:str):

    za = sorted(lista_paises, key=itemgetter(parametro), reverse=True)
    print(Back.LIGHTGREEN_EX + Fore.BLACK +"""
============================================ LISTA ORDENADA: DESCENDIENTE ============================================""")
    for i in range(len(za)):
        print(f"""Nombre: {za[i]["nombre"].capitalize()}  Poblacion: {za[i]["poblacion"]}  Superficie: {za[i]["superficie"]}km2  Continente: {za[i]["continente"].capitalize()}""")
        print(Fore.BLACK + "--------------------------------------------------------")
    print(Back.LIGHTGREEN_EX + Fore.BLACK +"=============== FIN DE LISTA ===============")    
    pausar_menu = input("Pulse ENTER para continuar: ")
    os.system('cls')

