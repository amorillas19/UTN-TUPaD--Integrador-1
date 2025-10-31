from f_filtros import menu_continente, menu_poblacion, menu_superficie

#Sirve de menu para la opcion 2, le pide al usuario el parametro sobre el cual filtrar y en base a eso se
#llama a las funciones pertinentes

def filtrar_paises():
    bandera_filtro = True
    print("""
    ========= FILTRO DE PAISES =========    
    [1] Por continente
    [2] Por Rango de población
    [3] Por rango de superficie
    """)


    while bandera_filtro:
        menu_filtro = input("Que opcion desea realizar: ")


        match menu_filtro:
            case "1":
                menu_continente()
                bandera_filtro = False
            case "2":
                menu_poblacion()
                bandera_filtro = False

            case "3":
                menu_superficie()
                bandera_filtro = False
            case _: 
                print("Opcion no valida")