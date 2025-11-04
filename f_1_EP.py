import os
from f_validaciones import validar_nombre
from colorama import Fore, Back, Style, init
init(autoreset=True)

#Si el string ingresado coincide exactamente con un pais entra en esta funcion
def busqueda_exacta(lista_paises:list, indice_exacto:int):
    try:
        i = indice_exacto
        
        print (Back.LIGHTBLACK_EX + Fore.WHITE + Style.BRIGHT + "=============== BUSQUEDA EXACTA ==================")
        print ("")
        print ("        " + Back.LIGHTWHITE_EX + Fore.WHITE + Style.BRIGHT + "Pais: ")
        print (f"""        {lista_paises[i]["nombre"].capitalize()} 
        Poblacion: {lista_paises[i]["poblacion"]} habitantes 
        Superficie: {lista_paises[i]["superficie"]} km2 
        Continente: {lista_paises[i]["continente"].capitalize()}""")
        print (Back.LIGHTBLACK_EX + Fore.WHITE + Style.BRIGHT + "==================================================")
        pausar_menu = input("Pulse ENTER para continuar: ")
        os.system('cls')
    
    except Exception as e:
        print (f"En funcion exacta: Ocurrio el error{type(e).__name__}: {e}")

#Si el string ingresado no coincide exacto, devuelve una lista de coincidencias
def busqueda_parcial(lista_paises:list, frase_buscar:str):

    try:
        
        lista_paises_coincidencia = []
        contador_paises_coincidencia = 0

        for pais in lista_paises:
            aux_name = str(pais["nombre"])
            if aux_name.find(frase_buscar) != -1:
                lista_paises_coincidencia.append(pais)
                contador_paises_coincidencia += 1


        print(Back.LIGHTWHITE_EX + Fore.BLACK + f"Usando el termino '{frase_buscar}', se encontraron {contador_paises_coincidencia} coincidencias:")
        print("")
        print (Back.LIGHTBLACK_EX + Fore.WHITE + Style.BRIGHT + "=============== BUSQUEDA PARCIAL ==================")
        for coincidencias in lista_paises_coincidencia:
            
            print (f"""
        Pais   :     {coincidencias["nombre"].capitalize()}
        Poblacion: {coincidencias["poblacion"]} habitantes 
        Superficie {coincidencias["superficie"]} km2 
        Continente: {coincidencias["continente"].capitalize()}""")
            print (Back.LIGHTBLACK_EX + Fore.WHITE + Style.BRIGHT + "==================================================")
        print ("")
        pausar_menu = input("Pulse ENTER para continuar: ")
        os.system('cls')


    except Exception as e:
        print (f"En funcion parcial: Ocurrio el error {type(e).__name__}:_ {e}")