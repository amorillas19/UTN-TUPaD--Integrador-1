import requests
import json
import csv

#Se llama la API y se construye un JSON para almacenar localmente datos
def armar_api():

    try:
        
        paises_lista_api = requests.get('https://restcountries.com/v3.1/all?fields=name,population,area,continents')
        datos_api = paises_lista_api.json()

        with open ("paises_api.json", "w", encoding='utf-8') as archivo:
            json.dump(datos_api, archivo, indent=2)

        print ("Archivo guardado exitosamente en un JSON")
        return datos_api    

    except Exception as e:
        print (f"Ocurrio el error {type(e).__name__}: {e}")


#Se procesa el JSON para que se convierta en una lista de diccionarios a trabajar
def procesar_json():

    try:
        procesar_api=armar_api()

        if procesar_api is None:
            return []
        
        lista_paises_procesados = []

        for pais in procesar_api:
            nombre = pais['name']['common']
            poblacion = pais['population']
            superficie = pais['area']
            continente = pais['continents']

            pais_completo = {
                'nombre' : nombre,
                'poblacion' : int(poblacion),
                'superficie' : float(superficie),
                'continente' : continente
            }

            lista_paises_procesados.append(pais_completo)

        print ("Paises añadidos exitosamente a la lista.")
        return lista_paises_procesados
    
    except Exception as e:
        print (f"Ocurrio el error {type(e).__name__}: {e}")


#Se escribe el csv local con los valores conseguidos
def escribir_csv():

    try:
        procesar_lista=procesar_json()

        with open("paises.csv", "w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writeheader()
            writer.writerows(procesar_lista)
        
        print("CSV armado exitosamente!")

    except Exception as e:
        print (f"Ocurrio el error {type(e).__name__}: {e}")        
        



if __name__ == "__main__":
    escribir_csv()