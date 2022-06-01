# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:37:28 2022

@author: migue
"""
#Importamos la libreria

import camelcase
# Tenemos una cadena llamada nombre y se desea que se muestre
# en formato título
nombre = "miguel Angel Yauricasa mendoza"

print(nombre.upper())
print(nombre.title())

# Creamos un objeto llamado cam

cam= camelcase.CamelCase()
print("Con camelcase...")

#Imprimimos el nombre en formato titulo
#Utilzamos camelcase
print(cam.hump(nombre))

#Para resolver el problema
#Creamos otro objeto cam2
#Al definir el objeto, incluimos los argumentos
# 'miguel' y 'mendoza'

cam2= camelcase.CamelCase('miguel','mendoza')
print(cam2.hump(nombre))