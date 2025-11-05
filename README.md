Proyecto Integrador -- Programacion 1

Integrantes: Ciro Cattáneo y Andrés Morillas

--------------------------------------------

Descripción del programa:
  Este proyecto, es una aplicación desarrollada en Python 3.13.7, diseñada con el principal objetivo de gestionar, analizar, y ofrecer estadisticas de distintos paises del mundo.
  Principalmente construida a partir de la obtención de datos provenientes de la pagina http://https://restcountries.com/; luego se forma un archivo JSON; para finalmente ser migrado a uno en formato .CSV
  Luego, mediante la utilizacion de distintas funcionalidades aprendidas durante el transcurso del año, es que se presenta al usuario un menu con distintas funcionalidades, que brndan en definitiva informacion sobre cada pais.

  El menu cumple distintas funcionalidades, tales como busqueda de paises por frases, preparado para devolver entradas por coincidencias tanto exactas como coincidencias parciales. Tambien se encarga de filtrar y/o ordenar paises en listas, por criterios a eleccion ofrecidos al usuario. Sea por cantidad de superficie territorial, poblacion, o continentes. Ademas de esto posee otras funciones como ordenar la lista segun poblacion, superficie u orden alfabetico y estadisticas varias, las cuales pueden ser: los paises con mayor y menor poblacion de toda la lista, el promedio de poblacion o de superficie por cada pais tomando en cuenta la lista en su totalidad.

--------------------------------------------

Instrucciones de uso:

El programa puede probarse y utiizarse desde tres lugares distintos:

1) Uso local:
   Mediante la descarga del proyecto integrador, ya sea mediante la utilización de Fork, o mediante la descarga del mismo.
   Se ejecuta por consola en la raiz del directorio utilizando el comando "python main.py"
   
2) Uso mediante Docker - (Local)
   Mediante la descarga del proyecto integrador, el mismo ya trae consigo incluidos los archivos necesarios para su ejecucion a través de Docker.
   Se debería crear una imagen del proyecto con el comando "docker build -t imagen_integrador ." y luego posteriormente utilizando el comando "docker run -it --rm -v ${PWD}:/app imagen_integrador" (Los comandos deben ser ingresados sin incluir las comillas)
   
3) Uso mediante Docker - (Cloud)
   Se ofrece un link al repositorio, y el correspondiente contenedor, subidos en https://hub.docker.com/repository/docker/agmorillas/tp_integrador_prog1/general


--------------------------------------------

Informe: Incluido en el repositorio
Link video: https://youtu.be/QZ8mSISLI8g?si=6oEvGoD5MrSgXwXW

