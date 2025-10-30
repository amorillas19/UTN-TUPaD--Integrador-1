import csv

#Funcion para que se arme una lista, donde cada pais es un diccionario con 4 claves y valores
def armar_lista():

    lista_paises = []

    with open ("Paises.csv", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            lista_paises.append({"nombre":fila["nombre"] ,
                                  "poblacion":int(fila["poblacion"]) , 
                                 "superficie":float(fila["superficie"]),
                                 "continente":fila["continente"]})
        
    return lista_paises


