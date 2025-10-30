import csv

#Funcion para que se arme una lista, donde cada pais es un diccionario con 4 claves y valores
def csv_cargar_lista():

    lista_paises = []

    with open ("paises.csv", "r") as archivo:
        
        listado = archivo.readlines()

        for i in range (1,len(listado)):
            listado[i] = listado[i].strip().split(",")

            nombre = listado [i][0]
            poblacion = listado [i][1]
            superficie = listado [i][2]
            continente = listado [i][3]

            pais = {"nombre":nombre, 
                                "poblacion":poblacion,
                                "superficie":superficie,
                                "continenete":continente
                                }
            lista_paises.append(pais)
    
    for pais in lista_paises:
        print(pais)

if __name__ == "__main__":

    csv_cargar_lista()