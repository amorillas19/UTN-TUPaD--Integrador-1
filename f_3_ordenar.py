import os
import f_cargar_lista
from operator import itemgetter
from f_validaciones import validar_minimo_maximo
from f_varias import normalizar_pais, imprimir_solo_diez
from colorama import Fore, Back, Style, init
init(autoreset=True)


#Sirve para ordenar la lista en base a los parametros ingresados por el usuario, ademas permite ordenar la
#lista en orden inverso 

def ordenar_andres_a_to_z(lista_paises:list, parametro:str):

    az = sorted(lista_paises, key=itemgetter(parametro))
    print(Back.LIGHTGREEN_EX + Fore.BLACK +"""
============================================ LISTA ORDENADA: ASCENDIENTE ============================================""")
    imprimir_solo_diez(az)
    print(Back.LIGHTGREEN_EX + Fore.BLACK +"=============== FIN DE LISTA ===============")
    pausar_menu = input("Pulse ENTER para continuar: ")
    os.system('cls')
    

def ordenar_andres_z_to_a(lista_paises:list, parametro:str):

    za = sorted(lista_paises, key=itemgetter(parametro), reverse=True)
    print(Back.LIGHTGREEN_EX + Fore.BLACK +"""
============================================ LISTA ORDENADA: DESCENDIENTE ============================================""")
    imprimir_solo_diez(za)
    print(Back.LIGHTGREEN_EX + Fore.BLACK +"=============== FIN DE LISTA ===============")    
    pausar_menu = input("Pulse ENTER para continuar: ")
    os.system('cls')

if __name__ == "__main__":
    
    lista_main = f_cargar_lista.csv_to_lista()
    ordenar_andres_a_to_z(lista_main, "nombre")