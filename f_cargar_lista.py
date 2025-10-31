import csv
from f_varias import limpiar_continente, traducir_continente

#Funcion para que usando el CSV arme una lista de paises, donde cada pais es un diccionario con 4 claves y valores
def csv_cargar_lista():

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

    csv_cargar_lista()
   