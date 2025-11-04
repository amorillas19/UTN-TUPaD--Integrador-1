import os
from f_4_estadisticas import paises_menor_mayor_poblacion, promedio_poblacion, promedio_superficie, cantidad_continente
from colorama import Fore, Back, Style, init
init(autoreset=True)

#Sirve de menu para la opcion 4 y en base a eso llamar a las posibles funciones para sacar las estadisticas
#del .csv
def  estadisticas_paises (lista_paises):
    try:
        while True:
            print(Back.LIGHTMAGENTA_EX + Fore.BLACK + "Opcion 4. Estadisticas de paises.")
            print("")
            print(Back.LIGHTMAGENTA_EX + Fore.BLACK + "=============== ESTADISTICAS ================")
            print(Back.LIGHTWHITE_EX + Fore.BLACK + """        [1] Pais con mayor y menor poblacion 
        [2] Promedio de poblacion            
        [3] Promedio de superficie           
        [4] Cantidad de paises por continente
        [5] Volver al menu principal         """)
            print(Back.LIGHTMAGENTA_EX + Fore.BLACK + "=============================================")
            menu_estadisticas = input("Que opcion desea realizar: ")
            os.system('cls')

            match menu_estadisticas:

                case "1":
                    paises_menor_mayor_poblacion(lista_paises)

                case "2":
                    promedio_poblacion(lista_paises)

                case "3":
                    promedio_superficie(lista_paises)

                case "4":
                    cantidad_continente(lista_paises)

                case "5":
                    pausar_menu = input("Volviendo al menu principal. Pulse ENTER. ")
                    os.system('cls')
                    break

                case _:
                    print ("Opcion no valida")

    except Exception as e:
        print (f"En funcion general: Ocurrio el error {type(e).__name__}: {e}")  
    



