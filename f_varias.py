#Funcion sencilla que viene a limpiar los datos de en que continente
#Existe cada pais. Algunos existen en dos continentes (se simplifico a uno)
#Y todos, venian en formato lista. Se convirtieron a formato string.
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
def normalizar_pais(pais:str)->str:

    pais = pais.replace("é", "e")
    pais = pais.replace("ã", "a")
    pais = pais.capitalize()

    return pais

def imprimir_solo_diez (lista:list):
    cont = 0 
    bandera_imprimir = True
    
    while bandera_imprimir:
        for i in range(10):
            if cont <len(lista):
                print(f"""nombre: {lista[cont]["nombre"].capitalize()}   poblacion: {lista[cont]["poblacion"]}  superficie: {lista[cont]["superficie"]} km2  continente: {lista[cont]["continente"]}
--------------------------------------------------------------------------------------------------------- """)
            cont +=1
        bandera_opcion = True
        if cont <len(lista): 
            while bandera_opcion:
                opcion = input("Desea seguir imprimiendo paises[S/N]:  ").strip().lower()

                match opcion:
                    case "n":
                        bandera_opcion = False
                        bandera_imprimir = False

                    case "s":
                        bandera_opcion = False

                    case _:
                        print("Opcion no valida")
        else:
            bandera_opcion = False
            bandera_imprimir = False

if __name__ == "__main__":

    normalizar_pais("Saint Barthélemy")
