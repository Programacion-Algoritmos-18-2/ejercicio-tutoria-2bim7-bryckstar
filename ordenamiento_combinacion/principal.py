"""
    Ejemplo tomado de 
    http://www.pythondiario.com/2018/08/ordenamiento-por-mezcla-merge-sort.html
"""
from modelado.combinacion import *  # Se importa todo de el archivo combinado
from paquete_archivos.miarchivo import MiArchivo  # Se impota la clase MiArchivo
from modelado.persona import Persona  # Se importa la clase Persona

m = MiArchivo()  # Se crea un objeto de tipo MiArchivo

lista = m.obtener_informacion()  #  Se leen los datos del archivo

lista = [l.split(";") for l in lista]

lista_edad = []  # Se ccrea una lista para almecenar las edades

for d in lista:  # Ciclo para recorrer los datos
	p = Persona(d[0], d[1], int(d[2]))  # Se crea un objeto del ipo persona con lo datos
	lista_edad.append(p.getEdad())  # Se agrega a la lista laa edades de las personas

print(lista_edad)  # Se imprime la lista de edades

merge_sort_result = merge_sort(lista_edad)  # Se llama al metodo para ordenar

print(merge_sort_result)  # Se imprime la lista ordenada

