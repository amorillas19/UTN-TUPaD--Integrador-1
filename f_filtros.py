from f_cargar_lista import csv_cargar_lista
from f_validaciones import validar_minimo_maximo

def menu_continente():
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
                filtrar_continente(opcion_continente)
                bandera_continente = False
            
            case "2":
                opcion_continente = "américa del sur" 
                print(filtrar_continente(opcion_continente))
                bandera_continente = False
                
            case "3":
                opcion_continente = "europa" 
                print(filtrar_continente(opcion_continente))
                bandera_continente = False
                
            case "4":
                opcion_continente = "africa" 
                print(filtrar_continente(opcion_continente))
                bandera_continente = False
                

            case "5":
                opcion_continente = "asia" 
                print(filtrar_continente(opcion_continente))
                bandera_continente = False
                

            case "6":
                opcion_continente = "oceania" 
                print(filtrar_continente(opcion_continente))
                bandera_continente = False
                

            case "7":
                opcion_continente = "antártida" 
                print(filtrar_continente(opcion_continente))
                bandera_continente = False

            case _:
                print("Opcion invalida")
                





def filtrar_continente (filtro:str):
    print(filtro)
    lista_paises = csv_cargar_lista()
    lista_filtrada = []

    for i in lista_paises :
        if i["continente"] == filtro:
            lista_filtrada.append(i)
            
    for i in lista_filtrada:
        print(f"{i}\n")

    


def menu_poblacion ():
    print("""
    ============ POBLACION ============

""")
    minimo, maximo = validar_minimo_maximo()
    filtrar_poblacion(minimo,maximo)
    



def filtrar_poblacion(min:int,max:int)->list:
    lista_paises = csv_cargar_lista()
    lista_poblacion = []
    for i in lista_paises:
        if (i["poblacion"] >= min) and (i["poblacion"] <= max):
            lista_poblacion.append(i)
    for i in lista_poblacion:
        print (f"{i}\n")





def menu_superficie():
    print("========== SUPERFICIE ==========")

    minimo, maximo = validar_minimo_maximo()
    filtrar_superficie(minimo,maximo)



def filtrar_superficie(min:int , max:int)->list:
    lista_paises = csv_cargar_lista()
    lista_superficie = []
    for i in lista_paises:
        if (i["superficie"] >= min) and (i["superficie"] <= max):
            lista_superficie.append(i)
    for i in lista_superficie:
        print (f"{i}\n")


