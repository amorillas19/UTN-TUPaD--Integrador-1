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
                ordenar(entrada)
                bandera_ordenar = False
            case "2":
                entrada = "poblacion"
                ordenar(entrada)
                bandera_ordenar = False

            case "3":
                entrada = "superficie"
                ordenar(entrada)
                bandera_ordenar = False

            case _:
                print("Opcion no valida")



def ordenar(entrada:str):
    lista__original = csv_cargar_lista()
    lista_paises = csv_cargar_lista()

    for i in range (len(lista_paises)-1):
        cambio = False
        for j in range(0 , len(lista_paises) -i -1):

            if lista_paises[j][entrada] > lista_paises[j+1][entrada]:
                
                lista_paises[j] , lista_paises[j+1] = lista_paises[j+1] , lista_paises[j]
                cambio = True
        if not cambio:
            break

        
    for i in lista_paises:
        print(f"{i}\n")