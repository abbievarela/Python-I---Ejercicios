#🐍 Clase 00 — Hello World explicado
#print() — Mostrar texto en pantalla
# Esto es un comentario de una línea

### Hola Mundo ###
print("Hola Python")   # Con comillas dobles ✓
print('Hola Python')   # Con comillas simples ✓ (ambas funcionan igual)

"""
Este es un comentario
de varias líneas (con comillas dobles)
"""

'''
Este también es un comentario
de varias líneas (con comillas simples)
'''

#Los comentarios sirven para explicar tu código. Python no los ejecuta.

#type() — Ver qué tipo de dato es algo
'''
print(type("Soy un dato str"))  # <class 'str'>    → texto
print(type(5))                  # <class 'int'>    → número entero
print(type(1.5))                # <class 'float'>  → número decimal
print(type(3 + 1j))             # <class 'complex'>→ número complejo
print(type(True))               # <class 'bool'>   → verdadero/falso
print(type(print("Mi cadena"))) # <class 'NoneType'>→ sin valor de retorno
'''