from f_armar_lista import armar_lista

def menu_continente():
    bandera_continente = True
    print("""
============== CONTINENTES ==============
          
[1] America del Norte y Centro America
[2] America del Sur
[3] Europa
[4] Africa
[5] Asia
[6] Oceania
[7] Antartica 

=========================================
""")
    while bandera_continente:
        opcion_continente = input("Que continente desea buscar: ").strip()
        match opcion_continente:
            case "1":
                opcion_continente = "North America"
                print(filtrar_continente(opcion_continente))
                bandera_continente = False
            
            case "2":
                opcion_continente = "South America"
                print(filtrar_continente(opcion_continente))
                bandera_continente = False
                
            case "3":
                opcion_continente = "Europe"
                print(filtrar_continente(opcion_continente))
                bandera_continente = False
                
            case "4":
                opcion_continente = "Africa"
                print(filtrar_continente(opcion_continente))
                bandera_continente = False
                

            case "5":
                opcion_continente = "Asia"
                print(filtrar_continente(opcion_continente))
                bandera_continente = False
                

            case "6":
                opcion_continente = "Oceania"
                print(filtrar_continente(opcion_continente))
                bandera_continente = False
                

            case "7":
                opcion_continente = "Antarctica"
                print(filtrar_continente(opcion_continente))
                bandera_continente = False

            case _:
                print("Opcion invalida")
                





def filtrar_continente (filtro)->list:

    lista_paises = armar_lista()
    lista_filtrada = []

    for i in range (len (lista_paises) ):
        if lista_paises[i]["continente"] == filtro:
            lista_filtrada.append(lista_paises[i])
    
    return lista_filtrada

    
