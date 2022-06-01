# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:47:03 2022

@author: migue
"""

#Dado el subtotal, calcular el IGV y el total

import Financieros
subtotal = 800.77
print(f"Subtotal: {subtotal}")
print(f"IGV: {Financieros.obtenerIGVSubtotal(subtotal): .2f}")
print(f"Total: {Financieros.obtenerTotalconSubtotal(subtotal): .2f}")
