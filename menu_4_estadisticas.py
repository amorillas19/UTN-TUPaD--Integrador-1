#Sirve de menu para la opcion 4 y en base a eso llamar a las posibles funciones para sacar las estadisticas
#del .csv
def  estadisticas_paises (lista_paises):
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
                promedio_poblacion(lista_paises)
                bandera_estadisticas = False

            case "3":
                promedio_superficie(lista_paises)
                bandera_estadisticas = False

            case "4":
                cantidad_continente(lista_paises)
                bandera_estadisticas = False

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
def promedio_poblacion (lista_paises):
    suma = 0
    for i in lista_paises:
        suma += i["poblacion"]
    print(f"""
========================= PROMEDIO POBLACION =========================          
El promedio de poblacion mundial es de {suma/len(lista_paises)} personas por pais 
======================================================================
""")
    

#Sirve para sacar el promedio de superficie por pais a nivel mundial
def promedio_superficie (lista_paises):
    suma = 0
    for i in lista_paises:
        suma += i["superficie"]
    print(f"""
========================= PROMEDIO SUPERFICIE =========================          
El promedio de superficie mundial es de {suma/len(lista_paises)} km2 por pais 
=======================================================================
""")
    

#Sirve para mostrar cantidad de paises por cada continente
def cantidad_continente(lista_paises):

    cant_europa = contar_paises_continente("europa")
    cant_Namerica = contar_paises_continente("américa del norte")
    cant_Samerica = contar_paises_continente("américa del sur")
    cant_africa = contar_paises_continente("africa")
    cant_asia = contar_paises_continente("asia")
    cant_oceania = contar_paises_continente("oceania")
    cant_antartida = contar_paises_continente("antártida")

    print(f"""
============== CANTIDAD POR CONTINENTE ==============          
Europa tiene {cant_europa} paises
-----------------------------------------------------
America del norte y Centroamerica tienen {cant_Namerica} paises
-----------------------------------------------------
America del sur tiene {cant_Samerica} paises
-----------------------------------------------------
Africa tiene {cant_africa} paises
-----------------------------------------------------
Asia tiene {cant_asia} paises
-----------------------------------------------------
Oceania tiene {cant_oceania} paises
-----------------------------------------------------
Antartida tiene {cant_antartida} paises
=====================================================
          
          """)
    
#Sirve para contar cuantos paises hay en un continente en especifico
def contar_paises_continente (lista_paises, continente:str) -> int:

    cont = 0
    for i in lista_paises:
        if i["continente"] == continente:
            cont +=1

    return cont