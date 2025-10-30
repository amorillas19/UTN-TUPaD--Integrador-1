
#Funcion general para validar el ingreso de una palabra
def validar_nombre (nombre_p :str)-> str :
    
    nombre_p = nombre_p.lower()

    if nombre_p == "" or not(nombre_p.isalpha()):
        print("No se pueden ingresar numeros, o dejar el campo vacio")
        while (nombre_p == "" or not(nombre_p.isalpha())):
            nombre_p :str = input("Que pais desea buscar? ")
    
    return nombre_p


if __name__ == "__main__":

    print ("Probando validaciones...")

    nombre_1 = "111"
    resultado = validar_nombre(nombre_1)
    print(f"Prueba con {nombre_1}: {resultado}")