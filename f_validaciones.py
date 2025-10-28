def validar_nombre(nombre_p :str) -> str : # type: ignore
    
    if nombre_p == "" or not(nombre_p.isalpha()):
        print("No se pueden ingresar numeros, o dejar el campo vacio")
        while (nombre_p == "" or not(nombre_p.isalpha())):
            nombre_p :str = input("Que pais desea buscar? ")
    
    return nombre_p


if __name__ is "main":

    