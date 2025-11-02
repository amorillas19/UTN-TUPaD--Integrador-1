import os
from f_filtros import menu_continente, menu_poblacion, menu_superficie
from colorama import Fore, Back, Style, init
init(autoreset=True)

#Sirve de menu para la opcion 2, le pide al usuario el parametro sobre el cual filtrar y en base a eso se
#llama a las funciones pertinentes

def filtrar_paises(lista_paises: list):
    bandera_filtro = True

    print(Back.LIGHTBLUE_EX + Fore.BLACK + "Opcion 2. Filtrar paises.")
    print("")
    print(Back.LIGHTBLUE_EX + Fore.BLACK + "====== FILTRO DE PAISES =======")
    print(Back.LIGHTWHITE_EX + Fore.BLACK +"""    [1] Por continente         
    [2] Por Rango de población 
    [3] Por rango de superficie""")
    print(Back.LIGHTBLUE_EX + Fore.BLACK + "===============================")
    print("")


    while bandera_filtro:
        menu_filtro = input(Back.LIGHTWHITE_EX + Fore.BLACK + "Que opcion desea realizar: ")
        print("")
        os.system('cls')


        match menu_filtro:
            case "1":
                menu_continente(lista_paises)
                bandera_filtro = False
            case "2":
                menu_poblacion(lista_paises)
                bandera_filtro = False

            case "3":
                menu_superficie(lista_paises)
                bandera_filtro = False
            case _: 
                print("Opcion no valida")