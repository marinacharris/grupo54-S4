# Una tupla es una colección de datos que se utiliza para guardar varios 
# elementos
# Las tuplas son ordenadas e indexadas
# las tuplas son inmutables

frutas = ('manzana', 'piña', 'pera')
print(frutas)
print(type(frutas))
print(frutas[2])
#frutas[2] = 'coco' -> no se hace, porque las tuplas son inmutables

tupla1 = ('Juan', 50, True, [50, 25, 40])
print(tupla1)
tupla1[3][1] = 100
print(tupla1)

def operaciones(a,b):
    suma = a+b
    resta = a-b 
    mult = a*b 
    div = a/b 
    return suma, resta, mult, div

resultados = operaciones(50,100)
print(resultados)
print(type(resultados))

a = (3,) # Si la tupla es de un solo elemento, entonces se le coloca una coma
b = ('Marina',)
c = (True,)
print(type(a), type(b), type(c))
tupla2 = (8,5,4,7,8,5)
lista = list(tupla2)
print(tupla2, lista)

