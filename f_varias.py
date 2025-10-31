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

if __name__ == "__main__":

    limpiar_continente("['Europe', 'Asia']")
