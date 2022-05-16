# Realice un programa que lea el código de un producto como llave de un 
# diccionario y en dicha llave va a almacenar nombre, precio y cantidad 
# del producto en una lista.
# El programa debe permitir cargar datos al diccionario, debe mostrar 
# un listado completo del diccionario y debe permitir consultar un producto 
# por su llave.

# Aplicación CRUD, create, read, update, delete
# V2, Agregar que se pueda actualizar precio y/o cantidad de un producto
# y que se pueda borrar productos

def prueba():
    pass

def crear(productos):
    codigo = int(input('Ingrese el codigo del producto\n'))
    nombre = input('Ingrese el nombre del producto\n')
    precio = int(input('Ingrese el precio del producto\n'))
    cantidad = int(input('Igrese el cantidad del producto\n'))
    productos.setdefault(codigo,[nombre,precio,cantidad])
    return productos
    
def mostrar(productos):
    print('Listado de Productos')
    print('Codigo', 'Nombre', 'Precio', 'Cantidad', sep = '\t\t')    
    for i in productos:
        print(i, productos[i][0], productos[i][1], productos[i][2], sep="\t\t")
    
def consultar(productos):
    cod = int(input ('Ingrese el cod del producto\n'))
    if cod in productos:
        print(productos[cod][0], productos[cod][1], productos[cod][2])
    else:
        print('El código del producto no existe')
        
    
def actualizar(productos):
    cod = int(input('Digite el código del producto que desea actualizar\n'))
    if cod in productos:
        precio = int(input('Digite el precio\n'))
        cantidad = int(input('Digite el cantidad del producto\n'))
        productos[cod][1] = precio 
        productos[cod][2] = cantidad
        print('Producto actualizado:', productos[cod])
    else:
        print('El código del producto no existe')
        
def borrar(productos):
    cod = int(input('Digite el código del producto que desea eliminar'))
    if cod in productos:
        print('Producto eliminado:', productos.pop(cod))
    else:
        print('El código del producto no existe')          
   

continuar = 's'
productos = {
    1:['manzana', 2500, 80],
    2:['pera', 3000, 90],
    3:['banana', 500, 1500]
}
while continuar =='s' or continuar == 'S':
    print('MENU')
    print('1. Crear producto')
    print('2. Mostar producto')
    print('3. Consultar')
    print('4. Actualizar cantidad y precio')
    print('5. Eliminar producto')
    opcion = int(input(f'Digite una de las tres opciones [1,2,3,4,5]\n'))
    if opcion == 1:
        crear(productos)
        print('Producto creado')
    elif opcion == 2:
        mostrar(productos)
    elif opcion == 3:   
        consultar(productos)
    elif opcion == 4:
        actualizar(productos)
    elif opcion == 5:        
        borrar(productos)
    else:
        print('Digita una opción válida')
    continuar = input('Presione "s" para continuar o cualquier letra para salir')
    
        
