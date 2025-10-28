from f_validaciones import validar_nombre

def buscar_paises():
    opcion_busqueda :str = input("Que pais desea buscar? ")
    opcion_busqueda = validar_nombre(opcion_busqueda)

    
