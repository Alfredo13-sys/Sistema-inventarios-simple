import csv

productos = list()

def AgregarProductoNuevo():
    opc = 0
    while(opc != 2):
        opc = int(input('1- agregar producto\n2- salir\n'))
        if (opc == 1):
            nombre = input("Nombre del producto: ")
            stock = input("Numero de productos: ")
            precio = input("Precio del producto: ")
            producto = dict()
            producto['nombre'] = nombre
            producto['stock'] = stock
            producto['precio'] = precio
            productos.append(producto)
            EscribirProductoNuevo()
            productos.clear()
        else:
            opc=2
            print("adios")

def EscribirProductoNuevo():
    with open('inventario.csv','a',newline='') as fichero:
        encabezado = ['nombre','stock','precio']
        escritor = csv.DictWriter(fichero,fieldnames=encabezado)
        escritor.writerows(productos)

def Creararchivo():
    with open('inventario.csv','w',newline='') as fichero:
        print("Fichero creado correctamente")
        encabezado = ['nombre','stock','precio']
        escritor = csv.DictWriter(fichero,fieldnames=encabezado)
        escritor.writeheader()

def LeerStock():
    with open('inventario.csv','r',newline='') as fichero:
        lector = csv.DictReader(fichero)
        for linea in lector:
            productos.append(linea)
    return productos

def ModificarStock(productos):
    stock = LeerStock()
    print(stock)
    modificar = int(input("Que elemento deseas modificar"))
    if modificar <= len(stock):
        print(stock[modificar-1])

ModificarStock(productos)