from f_armar_lista import armar_lista
from f_filtros import menu_continente

lista_paises = armar_lista()

def filtrar_paises():
    #Funcion de la opcion 2 del menu
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

            case "2":
                pass

            case "3":
                pass
            
            case _: 
                pass