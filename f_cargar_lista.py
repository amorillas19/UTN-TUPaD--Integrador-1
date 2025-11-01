import api_build
import os
import csv
from f_varias import limpiar_continente, traducir_continente

#Esta funcion es la mas importante, porque la utilizan las cuatro opciones, y llama a la funcion de api - Andres
#Funcion para que usando el CSV arme una lista de paises, donde cada pais es un diccionario con 4 claves y valores

def csv_to_lista():

    if not os.path.exists("paises.csv"):
        print("El archivo CSV NO ya existe")
        api_build.dict_to_csv()
    else:
        print("El archivo CSV EXISTE!!!")

    lista_paises = []

    with open ("paises.csv", "r") as archivo:
        reader = csv.DictReader(archivo)

        for linea in reader:

            nombre = linea["nombre"].lower()

            poblacion = int(linea["poblacion"])

            superficie = int(float(linea["superficie"]))

            continente = linea["continente"]
            continente = traducir_continente(limpiar_continente(continente))

            pais = {"nombre":nombre, 
                    "poblacion":poblacion,
                    "superficie":superficie,
                    "continente":continente
                    } 
            lista_paises.append(pais)
    
    return lista_paises

if __name__ == "__main__":

    csv_to_lista()
   