
#Funcion general para validar el ingreso de una palabra
def validar_nombre (nombre_p :str)-> str :
    
    nombre_p = nombre_p.lower()

    if nombre_p == "" or not(nombre_p.isalpha()):
        print("No se pueden ingresar numeros, o dejar el campo vacio")
        while (nombre_p == "" or not(nombre_p.isalpha())):
            nombre_p :str = input("Que pais desea buscar? ")
    
    return nombre_p


#Funcion general para validar el ingreso de un numero (debe ingresar como str)
def validar_numero_positivo(num:str)->bool:
    if num.isdigit():
        num = int(num)
        if num > 0 :
            return True
        
    return False
        

#Devuelve dos enteros forma de usar:   min, max = validar_minimo_maximo()   
#el min va a tomar el primer valor de salida y el max el segundo 
def validar_minimo_maximo()->int:
    bandera_min = True
    bandera_max = True

    while bandera_min:

        minimo = input("Ingrese el parametro minimo: ")

        if validar_numero_positivo(minimo):
            minimo_int = int(minimo)
            bandera_min = False

        else:
            print("El parametro minimo no es valido")


    while bandera_max:

        maximo = input("Ingrese el parametro maximo: ")

        if validar_numero_positivo(maximo):
            maximo_int = int(maximo)
            bandera_max = False
    
        else:
            print("El parametro maximo no es valido")
    return minimo_int,maximo_int



if __name__ == "__main__":

    print ("Probando validaciones...")

    nombre_1 = "111"
    resultado = validar_nombre(nombre_1)
    print(f"Prueba con {nombre_1}: {resultado}")