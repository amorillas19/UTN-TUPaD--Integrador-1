from f_validaciones import validar_nombre
from f_cargar_lista import csv_cargar_lista

#Funcion de la opcion 1 del menu
try:
    
    def buscar_paises():
        opcion_busqueda :str = input("Que pais desea buscar? ")
        opcion_busqueda = validar_nombre(opcion_busqueda)

        lista_paises = csv_cargar_lista()

        if lista_paises is None:
            print("Lista vacia")
        else:
            for i in range(1,len(lista_paises)):
                if opcion_busqueda == lista_paises[i]["nombre"]:
                    print("====BUSQUEDA EXACTA====")
                    print(f"Estoy en el numero: {i}")
                    print(f"""
                            Pais -- {lista_paises[i]["nombre"].capitalize()}: 
                            Poblacion: {lista_paises[i]["poblacion"]} habitantes, 
                            Superficie {lista_paises[i]["superficie"]} km2, 
                            Continente: {lista_paises[i]["continenete"].capitalize()}""")
                    print("============")

except Exception as e:
    print (f"Ocurrio el error {type(e).__name__}: {e}")   



if __name__ == "__main__":

    print(buscar_paises())

