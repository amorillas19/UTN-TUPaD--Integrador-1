import os
import f_cargar_lista
from f_validaciones import validar_minimo_maximo
from f_varias import normalizar_pais
from colorama import Fore, Back, Style, init
init(autoreset=True)

#Sirve para sacar el pais con menor y mayor poblacion de la lista 
def paises_menor_mayor_poblacion(lista_paises:list):

    #Sacamos el pais con menor poblacion
    pais_minimo = {}
    poblacion_minima = 100000000000000

    for i in lista_paises:
        if i["poblacion"] < poblacion_minima : 
            poblacion_minima = i["poblacion"]
            pais_minimo = i

    print(Back.LIGHTMAGENTA_EX + Fore.BLACK + "========== PAIS CON MENOR POBLACION ==========")
    print(f"""Nombre: {pais_minimo["nombre"]}.
----------------------------------------------
Poblacion: {pais_minimo["poblacion"]}.
----------------------------------------------
Superficie: {pais_minimo["superficie"]}.
----------------------------------------------
Continente: {pais_minimo["continente"]}.""")
    print("")

    #Sacamos el pais con mayor poblacion 
    pais_maximo = {}
    poblacion_maxima = 0

    for i in lista_paises:
        if i["poblacion"] > poblacion_maxima :
            poblacion_maxima = i["poblacion"]
            pais_maximo = i

    print(Back.LIGHTMAGENTA_EX + Fore.BLACK + "========== PAIS CON MAYOR POBLACION ==========")
    print(f"""Nombre: {pais_maximo["nombre"]}.
----------------------------------------------
Poblacion: {pais_maximo["poblacion"]}.
----------------------------------------------
Superficie: {pais_maximo["superficie"]}.
----------------------------------------------
Continente: {pais_maximo["continente"]}.""")
    print(Back.LIGHTMAGENTA_EX + Fore.BLACK + "============================================== ")
    pausar_menu = input("Pulse ENTER para continuar: ")
    os.system('cls')

#Sirve para sacar el promedio de poblacion por pais a nivel mundial
def promedio_poblacion (lista_paises):
    suma = 0
    for i in lista_paises:
        suma += i["poblacion"]
    
    print(Back.LIGHTMAGENTA_EX + Fore.BLACK + "========== PROMEDIO POBLACION ==========")
    print(f"""El promedio de poblacion mundial es de {suma/len(lista_paises)} personas por pais.""")
    print(Back.LIGHTMAGENTA_EX + Fore.BLACK + "============================================== ")
    pausar_menu = input("Pulse ENTER para continuar: ")
    os.system('cls')
    

#Sirve para sacar el promedio de superficie por pais a nivel mundial
def promedio_superficie (lista_paises):
    suma = 0
    for i in lista_paises:
        suma += i["superficie"]

    print(Back.LIGHTMAGENTA_EX + Fore.BLACK + "========== PROMEDIO SUPERFICIE ==========")
    print(f"""El promedio de superficie mundial es de {suma/len(lista_paises)} km2 por pais.""")
    print(Back.LIGHTMAGENTA_EX + Fore.BLACK + "============================================== ")
    pausar_menu = input("Pulse ENTER para continuar: ")
    os.system('cls')
    

#Sirve para mostrar cantidad de paises por cada continente
def cantidad_continente(lista_paises):

    cant_europa = contar_paises_continente(lista_paises, "europa")
    cant_Namerica = contar_paises_continente(lista_paises, "américa del norte")
    cant_Samerica = contar_paises_continente(lista_paises, "américa del sur")
    cant_africa = contar_paises_continente(lista_paises, "africa")
    cant_asia = contar_paises_continente(lista_paises, "asia")
    cant_oceania = contar_paises_continente(lista_paises, "oceania")
    cant_antartida = contar_paises_continente(lista_paises, "antártida")

    print(Back.LIGHTMAGENTA_EX + Fore.BLACK + "============= CANTIDAD POR CONTINENTE =============")
    print(f"""Europa tiene {cant_europa} paises.
-----------------------------------------------------
America del norte y Centroamerica tienen {cant_Namerica} paises.
-----------------------------------------------------
America del sur tiene {cant_Samerica} paises.
-----------------------------------------------------
Africa tiene {cant_africa} paises.
-----------------------------------------------------
Asia tiene {cant_asia} paises.
-----------------------------------------------------
Oceania tiene {cant_oceania} paises.
-----------------------------------------------------
Antartida tiene {cant_antartida} paises.""")
    print(Back.LIGHTMAGENTA_EX + Fore.BLACK + "==================================================== ")
    pausar_menu = input("Pulse ENTER para continuar: ")
    os.system('cls')
    
#Sirve para contar cuantos paises hay en un continente en especifico
def contar_paises_continente (lista_paises, continente:str) -> int:

    cont = 0
    for i in lista_paises:
        if i["continente"] == continente:
            cont +=1

    return cont

if __name__ == "__main__":
    pass