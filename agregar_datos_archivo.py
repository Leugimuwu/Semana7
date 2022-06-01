# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:57:32 2022

@author: migue
"""

archivo = open("noticia.txt","at")
#\n es para agregar el contenido en una linea final
contenido="\nFuente: YO"

archivo.write(contenido)
archivo.close()