from f_validaciones import validar_nombre
from f_armar_lista import armar_lista

#Funcion de la opcion 1 del menu
def buscar_paises():
    opcion_busqueda :str = input("Que pais desea buscar? ")
    opcion_busqueda = validar_nombre(opcion_busqueda)

    lista_paises = armar_lista()

      
    for i in range(1,len(lista_paises)):
        if opcion_busqueda == lista_paises[i]["nombre"]:
            print("====BUSQUEDA EXACTA====")
            print(f"""
                  Pais -- {lista_paises[i]["nombre"].capitalize()}: 
                  Poblacion: {lista_paises[i]["poblacion"]} habitantes, 
                  Superficie {lista_paises[i]["superficie"]} km2, 
                  Continente: {lista_paises[i]["continenete"].capitalize()}""")
            print("============")



if __name__ == "__main__":

    print(buscar_paises())

