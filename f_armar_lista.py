
#Funcion para que se arme una lista, donde cada pais es un diccionario con 4 claves y valores
def armar_lista():

    lista_paises = []

    with open ("paises.csv", "r") as archivo:
        lista_paises = archivo.readlines()

        for i in range (len(lista_paises)):
            lista_paises[i] = lista_paises[i].strip().split(",")
            lista_paises [i] = {"nombre":lista_paises[i][0], 
                                "poblacion":int(lista_paises[i][1]),
                                "superficie":float(lista_paises[i][2]),
                                "continenete":lista_paises[i][3]
                                }
    
    return lista_paises