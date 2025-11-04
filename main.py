import os
from f_cargar_lista import csv_to_lista
from menu_1_buscar import buscar_paises
from menu_2_filtrar import filtrar_paises
from menu_3_ordenar import ordenar_paises
from menu_4_estadisticas import estadisticas_paises
from colorama import Fore, Back, Style, init
init(autoreset=True)


while True:

    print("     " + Back.LIGHTCYAN_EX + Fore.BLACK + Style.BRIGHT + "==========================MENU DE OPERACIONES=========================")
    print("     " +Back.LIGHTWHITE_EX + Fore.BLACK + "1- Buscar un pais por nombre)                                         ")
    print("     " +Back.LIGHTWHITE_EX + Fore.BLACK + "2- Filtrar paises (continente, poblacion, superficie)                 ")
    print("     " +Back.LIGHTWHITE_EX + Fore.BLACK + "3- Ordenar paises (nombre, poblacion, superficie)                     ")
    print("     " +Back.LIGHTWHITE_EX + Fore.BLACK + "4- Mostrar estadisticas (poblacion, superficie, paises por continente)")
    print("     " +Back.LIGHTWHITE_EX + Fore.BLACK + "5- Salir                                                              ")
    print("     "+ Back.LIGHTCYAN_EX + Fore.BLACK+ Style.BRIGHT + "======================================================================")

    lista_main = csv_to_lista()

    print ("")
    opcion_menu :str = input ("     "+Back.LIGHTWHITE_EX + Fore.BLACK + "Que operación desea realizar: ")
    print("")
    if opcion_menu == "1":
        os.system('cls')
        buscar_paises(lista_main)

    elif opcion_menu == "2":
        os.system('cls')
        filtrar_paises(lista_main)
        
    elif opcion_menu == "3":
        os.system('cls')
        ordenar_paises(lista_main)

    elif opcion_menu == "4":
        os.system('cls')
        estadisticas_paises(lista_main)

    elif opcion_menu == "5":
        os.system('cls')
        print(Back.LIGHTBLACK_EX + Fore.BLACK + "Gracias por usar nuestro programa")
        break

    else:
        os.system('cls')
        print (Back.LIGHTBLACK_EX + Fore.BLACK +"Opcion no correcta")


      