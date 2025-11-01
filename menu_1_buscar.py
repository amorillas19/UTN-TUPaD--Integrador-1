from f_validaciones import validar_nombre

#Funcion de la opcion 1 del menu

def buscar_paises(lista_main : list):
    try:
        lista_paises = lista_main

        opcion_busqueda :str = input("Que pais desea buscar? ")
        opcion_busqueda = validar_nombre(opcion_busqueda)
        indice_exacto = 0

        for i in range (len(lista_paises)):
            if opcion_busqueda == lista_paises[i]["nombre"]:
                indice_exacto = i
                return busqueda_exacta(lista_paises, indice_exacto)
        
        return busqueda_parcial(lista_paises, opcion_busqueda)
        


    except Exception as e:
        print (f"En funcion general: Ocurrio el error {type(e).__name__}: {e}")   


def busqueda_exacta(lista_paises:list, indice_exacto:int):
    try:
        i = indice_exacto
        

        print (f"""
    ===============BUSQUEDA EXACTA==================
        Pais   :     {lista_paises[i]["nombre"].capitalize()}
            -------------------------- 

        Poblacion: {lista_paises[i]["poblacion"]} habitantes 

        Superficie {lista_paises[i]["superficie"]} km2 

        Continente: {lista_paises[i]["continente"].capitalize()}""")
        
        print ("    =========================================")
    
    except Exception as e:
        print (f"En funcion exacta: Ocurrio el error{type(e).__name__}: {e}")

def busqueda_parcial(lista_paises:list, frase_buscar:str):

    try:
        
        lista_paises_coincidencia = []
        contador_paises_coincidencia = 0

        for pais in lista_paises:
            aux_name = str(pais["nombre"])
            if aux_name.find(frase_buscar) != -1:
                lista_paises_coincidencia.append(pais)
                contador_paises_coincidencia += 1


        print(f"Usando el termino '{frase_buscar}', se encontraron {contador_paises_coincidencia} coincidencias:")

        for coincidencias in lista_paises_coincidencia:
            print (f"""
    ===============BUSQUEDA PARCIAL==================
        Pais   :     {coincidencias["nombre"].capitalize()}
            -------------------------- 

        Poblacion: {coincidencias["poblacion"]} habitantes 

        Superficie {coincidencias["superficie"]} km2 

        Continente: {coincidencias["continente"].capitalize()}""")
        
        print ("    =========================================")


    except Exception as e:
        print (f"En funcion parcial: Ocurrio el error {type(e).__name__}:_ {e}")



if __name__ == "__main__":
    busqueda_parcial("pe")
    

