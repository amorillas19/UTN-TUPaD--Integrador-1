import os
from f_validaciones import validar_minimo_maximo
from f_varias import normalizar_pais
from colorama import Fore, Back, Style, init
init(autoreset=True)


#Sirve para pedirle al usuario el continente a buscar y utilizarlo como parametro para llamar a la funcion
#filtrar_continente()

def menu_continente(lista_paises):
    bandera_continente = True
    print(Back.LIGHTBLUE_EX + Fore.BLACK + "============== CONTINENTES ===============")
    print(Back.LIGHTWHITE_EX + Fore.BLACK + """    [1] America del Norte y Centro America
    [2] America del Sur                   
    [3] Europa                            
    [4] Africa                            
    [5] Asia                              
    [6] Oceania                           
    [7] Antartica                         """)
    print(Back.LIGHTBLUE_EX + Fore.BLACK + "==========================================")

    while bandera_continente:
        opcion_continente = input(Back.LIGHTWHITE_EX + Fore.BLACK + "Que continente desea buscar: ").strip()
        print("")
        match opcion_continente:
            case "1":
                opcion_continente = "américa del norte" 
                filtrar_continente(lista_paises, opcion_continente)
                bandera_continente = False
            
            case "2":
                opcion_continente = "américa del sur" 
                filtrar_continente(lista_paises, opcion_continente)
                bandera_continente = False
                
            case "3":
                opcion_continente = "europa" 
                filtrar_continente(lista_paises, opcion_continente)
                bandera_continente = False
                
            case "4":
                opcion_continente = "africa" 
                filtrar_continente(lista_paises, opcion_continente)
                bandera_continente = False
                

            case "5":
                opcion_continente = "asia" 
                filtrar_continente(lista_paises, opcion_continente)
                bandera_continente = False
                

            case "6":
                opcion_continente = "oceania" 
                filtrar_continente(lista_paises, opcion_continente)
                bandera_continente = False
                

            case "7":
                opcion_continente = "antártida" 
                filtrar_continente(lista_paises, opcion_continente)
                bandera_continente = False

            case _:
                print("Opcion invalida")
                



#Toma el parametro de menu_continente () e imprime una lista de paises dentro de ese continente

def filtrar_continente (lista_paises, filtro:str):
    print()
    print(Back.LIGHTBLUE_EX + Fore.BLACK + f"""
=========================== PAISES DE {filtro.upper()} ===========================""")
    print("")
    lista_filtrada = []

    for i in lista_paises :
        if i["continente"] == filtro:
            nombre_filtrado= i["nombre"]
            nombre_filtrado = normalizar_pais(nombre_filtrado)
            poblacion_filtrada = i["poblacion"]
            superficie_filtrada = i["superficie"]
            pais_filtrado = {"nombre": nombre_filtrado, "poblacion": poblacion_filtrada, "superficie": superficie_filtrada}

            lista_filtrada.append(pais_filtrado)
            
    for i in lista_filtrada:
        print(Fore.BLACK + Style.BRIGHT + f"""Nombre: {i["nombre"]}       || Poblacion: {i["poblacion"]} habitantes       || Superficie: {i["superficie"]} km2""")
        print("-------------------------------------------------------------------------------------------")

    print ("")
    print(Back.LIGHTBLUE_EX + Fore.BLACK + """===================================================================================""")
    
    pausar_menu = input("Pulse ENTER para continuar: ")
    os.system('cls')

    

#En primer lugar llama a la funcion validar_minimo_maximo() para obtener dos int, los cuales va a utilizar
#para llamar a la funcion filtrar_poblacion()

def menu_poblacion (lista_paises):
    print(Back.LIGHTBLUE_EX + Fore.BLACK + """
=================== POBLACION ===================""")
    minimo, maximo = validar_minimo_maximo()
    print(Back.LIGHTBLUE_EX + Fore.BLACK + """
=============== FILTRO POBLACION ================""")
    filtrar_poblacion(lista_paises, minimo,maximo)
    print(Back.LIGHTBLUE_EX + Fore.BLACK +  """=================================================""")

    pausar_menu = input("Pulse ENTER para continuar: ")
    os.system('cls')




#Sirve para imprimir una lista con los parametros ingresados anteriormente, recorre la lista_paises y con
#un if comprueba si entrar en el rango adecuado, en el caso de que entren, son añadidos a lista_poblacion
#y luego son impresos
def filtrar_poblacion(lista_paises, min:int,max:int)->list:
    lista_poblacion = []
    for i in lista_paises:
        if (i["poblacion"] >= min) and (i["poblacion"] <= max):
            lista_poblacion.append(i)

    if len(lista_poblacion) == 0 :
        print (Back.LIGHTWHITE_EX + Fore.BLACK + "No se han encontrado paises con esos parametros. ")
    else:
        for i in lista_poblacion:
            print(Back.LIGHTWHITE_EX + Fore.BLACK + f"""Nombre: {i["nombre"].capitalize()} || Poblacion: {i["poblacion"]}""")
            print(Back.LIGHTWHITE_EX + Fore.BLACK + f"-------------------------------------------------")
    

def menu_superficie(lista_paises):
    print(Back.LIGHTBLUE_EX + Fore.BLACK +  """"
===================== SUPERFICIE =====================""")

    minimo, maximo = validar_minimo_maximo()
    filtrar_superficie(lista_paises, minimo,maximo)



def filtrar_superficie(lista_paises, min:int , max:int)->list:
    lista_superficie = []
    print(Back.LIGHTBLUE_EX + Fore.BLACK +  """
================= FILTRO SUPERFICIE ==================""")
    for i in lista_paises:
        if (i["superficie"] >= min) and (i["superficie"] <= max):
            lista_superficie.append(i)
    
    if len(lista_superficie) == 0 :
        print (Back.LIGHTWHITE_EX + Fore.BLACK + "No se han encontrado paises dentro de tales parametros")
    else:
        for i in lista_superficie:
            print (Back.LIGHTWHITE_EX + Fore.BLACK + f"""Nombre: {i["nombre"].capitalize()} || Superficie: {i["superficie"]} km2
------------------------------------------------------""")
    print(Back.LIGHTBLUE_EX + Fore.BLACK +  "======================================================")
    pausar_menu = input("Pulse ENTER para continuar: ")
    os.system('cls')


