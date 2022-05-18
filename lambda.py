#funcion lambda o función anónima
#sintaxis lambda:
# lambda argumentos: cuerpo de la función
conteo = lambda a: a+1
print(conteo(6), type(conteo))

def operaciones(a,b, fn):
    return fn(a,b)

suma = operaciones(10,8, lambda x,y: x+y)
print(suma)

resta = operaciones(25,19, lambda x,y: x-y)
print(resta)