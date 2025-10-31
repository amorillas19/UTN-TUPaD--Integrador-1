from f_cargar_lista import csv_cargar_lista

lista_paises = csv_cargar_lista()

def  estadisticas_paises ():
    print("""
========== ESTADISTICAS ==========
[1] Pais con mayor y menor poblacion          
[2] Promedio de poblacion         
[3] Promedio de superficie
[4] Cantidad de paises por continente        
          """)
    bandera_estadisticas = True

    while bandera_estadisticas:
        menu_estadisticas = input("Que opcion desea realizar: ")

        match menu_estadisticas:

            case "1":
                paises_menor_mayor_poblacion(lista_paises)
                bandera_estadisticas = False

            case "2":
                promedio_poblacion()
                bandera_estadisticas = False

            case "3":
                promedio_superficie()
                bandera_estadisticas = False

            case "4":
                pass

            case _:
                pass



#Sirve para sacar el pais con menor y mayor poblacion de la lista 
def paises_menor_mayor_poblacion(lista_paises:list):

    #Sacamos el pais con menor poblacion
    pais_minimo = {}
    poblacion_minima = 100000000000000

    for i in lista_paises:
        if i["poblacion"] < poblacion_minima : 
            poblacion_minima = i["poblacion"]
            pais_minimo = i

    print(f"""
========== PAIS CON MENOR POBLACION ==========
Nombre: {pais_minimo["nombre"]}
----------------------------------------------
Poblacion: {pais_minimo["poblacion"]}
----------------------------------------------
Superficie: {pais_minimo["superficie"]}
----------------------------------------------
Continente: {pais_minimo["continente"]}
==============================================      

      """)
    #Sacamos el pais con mayor poblacion 
    pais_maximo = {}
    poblacion_maxima = 0

    for i in lista_paises:
        if i["poblacion"] > poblacion_maxima :
            poblacion_maxima = i["poblacion"]
            pais_maximo = i

    print(f"""
========== PAIS CON MAYOR POBLACION ==========
Nombre: {pais_maximo["nombre"]}
----------------------------------------------
Poblacion: {pais_maximo["poblacion"]}
----------------------------------------------
Superficie: {pais_maximo["superficie"]}
----------------------------------------------
Continente: {pais_maximo["continente"]}
==============================================      

      """)

#Sirve para sacar el promedio de poblacion por pais a nivel mundial
def promedio_poblacion ():
    suma = 0
    for i in lista_paises:
        suma += i["poblacion"]
    print(f"""
========================= PROMEDIO POBLACION =========================          
El promedio de poblacion mundial es de {suma/len(lista_paises)} personas por pais 
======================================================================
""")
    




def promedio_superficie ():
    suma = 0
    for i in lista_paises:
        suma += i["superficie"]
    print(f"""
========================= PROMEDIO SUPERFICIE =========================          
El promedio de superficie mundial es de {suma/len(lista_paises)} km2 por pais 
=======================================================================
""")
    