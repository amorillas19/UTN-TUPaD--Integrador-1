import csv

#Funcion para que se arme una lista, donde cada pais es un diccionario con 4 claves y valores
def csv_cargar_lista():

    lista_paises = []

    with open ("paises.csv", "r") as archivo:
        reader = csv.DictReader(archivo)

        for linea in reader:
            nombre = linea["nombre"].lower()
            poblacion = linea["poblacion"]
            superficie = linea["superficie"]
            continente = linea["continente"]

            pais = {"nombre":nombre, 
                    "poblacion":poblacion,
                    "superficie":superficie,
                    "continenete":continente
                    }
            lista_paises.append(pais)
    
    for pais in lista_paises:
        print(pais)
        
    return lista_paises

if __name__ == "__main__":

    csv_cargar_lista()
   