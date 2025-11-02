def limpiar_continente (a:str)->str:
    
    a= a.lower()
    a = a.replace("[", "")
    a = a.replace("]", "")
    a = a.replace("'", "")
    a = a.strip().split(",")
    a = a[0]

    return a

def traducir_continente (cont:str)->str:

    if cont == "europe":
        cont = "europa"
    
    elif cont == "south america":
        cont = "américa del sur"

    elif cont == "north america":
        cont = "américa del norte"

    elif cont == "antarctica":
        cont = "antártida"

    return cont

#En los filtros del menu 2, intento reemplazar los caracteres rancios.
#En los filtros del menu 2, paso a mayusculas las iniciales
def normalizar_continente(cont:str)->str:

    cont = cont.replace("é", "e")
    cont = cont.replace("ã", "a")
    cont = cont.capitalize()

    return cont

if __name__ == "__main__":

    normalizar_continente("Saint Barthélemy")
