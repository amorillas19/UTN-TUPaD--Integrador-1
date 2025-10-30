from menu_buscar import buscar_paises
from menu_filtrar import filtrar_paises
while True:
    print('''
    ======MENU DE OPERACIONES======
        1- Buscar un pais por nombre
        2- Filtrar paises (continente, poblacion, superficie)
        3- Ordenar paises (nombre, poblacion, superficie)
        4- Mostrar estadisticas (poblacion, superficie, paises por continente)
        5- Salir
        ''')




    opcion_menu :str = input ("Que operación desea realizar: ")
    if opcion_menu == "1":
        buscar_paises()

    elif opcion_menu == "2":
        filtrar_paises()
        """
        Al parecer hay un problema para encontrar los continentes (En el csv son una lista)
        aparecen asi ["Asia"] , ["America] cuando deberian aparecer asi: Asia , America
            ¯\_(ツ)_/¯
        
        """
    elif opcion_menu == "3":
        print ("Ordenar paises")

    elif opcion_menu == "4":
        print ("Mostrar estadisticas")

    elif opcion_menu == "5":
        print("Gracias por usar nuestro programa")
        break

    else:
        print ("Opcion no correcta")


        