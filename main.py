from f_cargar_lista import csv_to_lista
from menu_1_buscar import buscar_paises
from menu_2_filtrar import filtrar_paises
from menu_3_ordenar import ordenar_paises
from menu_4_estadisticas import estadisticas_paises



while True:



    print('''
    ======MENU DE OPERACIONES======
        1- Buscar un pais por nombre
        2- Filtrar paises (continente, poblacion, superficie)
        3- Ordenar paises (nombre, poblacion, superficie)
        4- Mostrar estadisticas (poblacion, superficie, paises por continente)
        5- Salir
        ''')

    lista_main = csv_to_lista()


    opcion_menu :str = input ("Que operación desea realizar: ")
    if opcion_menu == "1":
        buscar_paises(lista_main)

    elif opcion_menu == "2":
        filtrar_paises(lista_main)
        
    elif opcion_menu == "3":
        ordenar_paises()

    elif opcion_menu == "4":
        estadisticas_paises()

    elif opcion_menu == "5":
        print("Gracias por usar nuestro programa")
        break

    else:
        print ("Opcion no correcta")


        