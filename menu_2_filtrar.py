import os
from f_2_filtros import menu_continente, menu_poblacion, menu_superficie
from colorama import Fore, Back, Style, init
init(autoreset=True)

#Sirve de menu para la opcion 2, le pide al usuario el parametro sobre el cual filtrar y en base a eso se
#llama a las funciones pertinentes
#Las funciones estan en un archivo aparte, denominado f_filtros
def filtrar_paises(lista_paises: list):
    try:
        while True:

            print(Back.LIGHTBLUE_EX + Fore.BLACK + "Opcion 2.")
            print("")
            print(Back.LIGHTBLUE_EX + Fore.BLACK + "========== FILTRO DE PAISES ============")
            print(Back.LIGHTWHITE_EX + Fore.BLACK +"""            [1] Por continente          
            [2] Por Rango de población  
            [3] Por rango de superficie 
            [4] Volver al menu principal""")
            print(Back.LIGHTBLUE_EX + Fore.BLACK + "========================================")
            print("")

            menu_filtro = input(Back.LIGHTWHITE_EX + Fore.BLACK + "Que opcion desea realizar: ")
            print("")
            os.system('cls')


            match menu_filtro:
                case "1":
                    menu_continente(lista_paises)

                case "2":
                    menu_poblacion(lista_paises)

                case "3":
                    menu_superficie(lista_paises)

                case "4":
                    pausar_menu = input("Volviendo al menu principal. Pulse ENTER. ")
                    os.system('cls')
                    break

                case _: 
                    print("Opcion no valida")
    except Exception as e:
        print (f"En funcion general: Ocurrio el error {type(e).__name__}: {e}")  
    