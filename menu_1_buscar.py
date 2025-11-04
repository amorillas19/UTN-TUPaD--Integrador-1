import os
from f_validaciones import validar_nombre
from f_1_EP import busqueda_exacta, busqueda_parcial
from colorama import Fore, Back, Style, init
init(autoreset=True)

#Funcion de la opcion 1 del menu
#Permite ingresar cualquier string, y dentro la logica decide
#Si se utiliza una busqueda total o parcial
def buscar_paises(lista_main : list):
    try:
        lista_paises = lista_main
        print(Back.RED + Fore.WHITE + Style.BRIGHT + "Opcion 1.")
        print("")
        print(Back.RED + Fore.WHITE + Style.BRIGHT + "======== BUSCAR PAISES ========")
        print("")
        print(Back.LIGHTWHITE_EX + Fore.BLACK + "Ingrese el nombre del pais, o una parte de su nombre: ")
        opcion_busqueda :str = input()
        print ("")
        opcion_busqueda = validar_nombre(opcion_busqueda)
        indice_exacto = 0

        for i in range (len(lista_paises)):
            if opcion_busqueda == lista_paises[i]["nombre"]:
                indice_exacto = i
                return busqueda_exacta(lista_paises, indice_exacto)
        
        return busqueda_parcial(lista_paises, opcion_busqueda)
        


    except Exception as e:
        print (f"En funcion general: Ocurrio el error {type(e).__name__}: {e}")   


if __name__ == "__main__":
    pass
    

