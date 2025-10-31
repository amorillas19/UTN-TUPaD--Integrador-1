from f_cargar_lista import csv_cargar_lista


def ordenar_paises ():
    bandera_ordenar = True
    print("""
========== ORDENAR PAISES ==========
[1] Ordenar por nombre
[2] Ordenar por poblacion
[3] Ordenar por superficie
          
          """)
    
    while bandera_ordenar:

        menu_ordenar = input("Que opcion desea realizar: ")

        match menu_ordenar:
            case "1":
                entrada = "nombre"
                revertir(entrada)
                bandera_ordenar = False

            case "2":
                entrada = "poblacion"
                revertir(entrada)
                bandera_ordenar = False

            case "3":
                entrada = "superficie"
                revertir(entrada)
                bandera_ordenar = False

            case _:
                print("Opcion no valida")



def revertir (entrada):
    bandera_reverir = True
    while bandera_reverir:
        print("""

[1] Ascendete
[2] Descendente      

""")
        respuesta = input("Desea ordenar de forma asccendente o descendente: ")
        match respuesta:
            case "1":

                ordenar(entrada,False)
                bandera_reverir = False

            case "2":
                ordenar(entrada,True)
                bandera_reverir = False

            case _:
                print("Opcion no valida")




def ordenar(entrada:str, revertir:None):
    lista_paises = csv_cargar_lista()

    for i in range (len(lista_paises)-1):
        cambio = False
        for j in range(0 , len(lista_paises) -i -1):

            if lista_paises[j][entrada] > lista_paises[j+1][entrada]:
                
                lista_paises[j] , lista_paises[j+1] = lista_paises[j+1] , lista_paises[j]
                cambio = True
        if not cambio:
            break

    if not revertir:
        for i in lista_paises:
            print(f"{i}\n")

    else:
        lista_paises.reverse()
        for i in lista_paises:
            print(f"{i}\n")