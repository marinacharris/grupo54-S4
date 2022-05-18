# convertir cadenas, se uitliza los constructores list, tuple y set

cadena= 'María'
lista = list(cadena)
print(lista, type(lista[0]))
conjunto = set(cadena)
print(conjunto)
# conversión de lista a cadena
lista = ['H', 'O','L', 'A']
cadena = ''.join(lista)
print(cadena)

#conversion a diccionario
cadena = "Colombia"
diccionario = dict(zip(range(len(cadena)),cadena))
print(diccionario)
Lista1 = ['Enero','Febrero','Marzo','Abril']
Lista2 = [50000000, 150000000, 80000000, 70000000]
diccionario2 = dict(zip(Lista1,Lista2))
print(diccionario2)
print(diccionario2.values())
print(diccionario2.items())
print(diccionario2.keys())


#conversion desde diccionarios

cadena = ''.join(diccionario.values())
print(cadena)