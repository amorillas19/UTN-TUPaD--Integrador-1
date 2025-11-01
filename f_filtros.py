
from f_validaciones import validar_minimo_maximo



#Sirve para pedirle al usuario el continente a buscar y utilizarlo como parametro para llamar a la funcion
#filtrar_continente()

def menu_continente(lista_paises):
    bandera_continente = True
    print("""
============== CONTINENTES ==============
          
[1] America del Norte y Centro America
[2] America del Sur
[3] Europa
[4] Africa
[5] Asia
[6] Oceania
[7] Antartica 

=========================================
""")
    while bandera_continente:
        opcion_continente = input("Que continente desea buscar: ").strip()
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
    print(f"""
=========================== PAISES DE {filtro.upper()} ===========================
          """)
    lista_filtrada = []

    for i in lista_paises :
        if i["continente"] == filtro:
            lista_filtrada.append(i)
            
    for i in lista_filtrada:
        print(f"""nombre: {i["nombre"]}  poblacion: {i["poblacion"]}  superficie: {i["superficie"]}
-----------------------------------------------------------------------------------""")

    print("""===================================================================================
          """)

    

#En primer lugar llama a la funcion validar_minimo_maximo() para obtener dos int, los cuales va a utilizar
#para llamar a la funcion filtrar_poblacion()

def menu_poblacion (lista_paises):
    print("""
=================== POBLACION ===================""")
    minimo, maximo = validar_minimo_maximo()
    print("""
=============== FILTRO POBLACION ================""")
    filtrar_poblacion(lista_paises, minimo,maximo)
    print("""=================================================""")




#Sirve para imprimir una lista con los parametros ingresados anteriormente, recorre la lista_paises y con
#un if comprueba si entrar en el rango adecuado, en el caso de que entren, son añadidos a lista_poblacion
#y luego son impresos
def filtrar_poblacion(lista_paises, min:int,max:int)->list:
    lista_poblacion = []
    for i in lista_paises:
        if (i["poblacion"] >= min) and (i["poblacion"] <= max):
            lista_poblacion.append(i)
    for i in lista_poblacion:
        print (f"""nombre: {i["nombre"]}  poblacion: {i["poblacion"]}
-------------------------------------------------""")
    





def menu_superficie(lista_paises):
    print(""""
===================== SUPERFICIE =====================""")

    minimo, maximo = validar_minimo_maximo()
    filtrar_superficie(lista_paises, minimo,maximo)



def filtrar_superficie(lista_paises, min:int , max:int)->list:
    lista_superficie = []
    print("""
================= FILTRO SUPERFICIE ==================""")
    for i in lista_paises:
        if (i["superficie"] >= min) and (i["superficie"] <= max):
            lista_superficie.append(i)
    for i in lista_superficie:
        print (f"""nombre: {i["nombre"]}  superficie: {i["superficie"]}
------------------------------------------------------""")
    print("======================================================")


