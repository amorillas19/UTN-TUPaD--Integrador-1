

#Sirve para pedir al usuario una opcion para ordenar los paises, en base a eso crea una entrada para
#la funcion revertir()

def ordenar_paises (lista_paises):
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
                revertir(lista_paises, entrada)
                bandera_ordenar = False

            case "2":
                entrada = "poblacion"
                revertir(lista_paises, entrada)
                bandera_ordenar = False

            case "3":
                entrada = "superficie"
                revertir(lista_paises, entrada)
                bandera_ordenar = False

            case _:
                print("Opcion no valida")


#Sirve para preguntar al usuario por el orden en el que se va a organizar la lista y en base a eso llamar
#a la funcion ordena()

def revertir (lista_paises, entrada):
    bandera_reverir = True
    while bandera_reverir:
        print("""

[1] Ascendete
[2] Descendente      

""")
        respuesta = input("Desea ordenar de forma asccendente o descendente: ")
        match respuesta:
            case "1":

                ordenar(lista_paises, entrada,False)
                bandera_reverir = False

            case "2":
                ordenar(lista_paises, entrada,True)
                bandera_reverir = False

            case _:
                print("Opcion no valida")



#Sirve para ordenar la lista en base a los parametros ingresados por el usuario, ademas permite ordenar la
#lista en orden inverso 
def ordenar(lista_paises, entrada:str, revertir:None):
    print("""
============================================ LISTA ORDENADA ============================================""")
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
            print(f"""Nombre: {i["nombre"]}  Poblacion: {i["poblacion"]}  Superficie: {i["superficie"]}  Continente: {i["continente"]}
--------------------------------------------------------------------------------------------------------""")

    else:
        lista_paises.reverse()
        for i in lista_paises:
           print(f"""Nombre: {i["nombre"]}  Poblacion: {i["poblacion"]}  Superficie: {i["superficie"]}  Continente: {i["continente"]}
--------------------------------------------------------------------------------------------------------""")
    print("""========================================================================================================""")