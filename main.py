print('''
======MENU DE OPERACIONES======
      1- Buscar un pais por nombre
      2- Filtrar paises (continente, poblacion, superficie)
      3- Ordenar paises (nombre, poblacion, superficie)
      4- Mostrar estadisticas (poblacion, superficie, paises por continente)
      5- Salir
      ''')

opcion_menu :str = input ("Que operación desea realizar: ")

while True:
    if opcion_menu == "1":
        print ("Buscar paises")

    elif opcion_menu == "2":
        print ("Filtrar paises")

    elif opcion_menu == "3":
        print ("Ordenar paises")

    elif opcion_menu == "4":
        print ("Mostrar estadisticas")

    elif opcion_menu == "5":
        break

    else:
        print ("Opcion no correcta")


        