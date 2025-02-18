import csv

productos = list()

def menu():
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
            AgregarProductoNuevo()
        else:
            opc=2
            print("adios")

def AgregarProductoNuevo():
    with open('inventario.csv','a',newline='') as fichero:
        encabezado = ['nombre','stock','precio']
        escritor = csv.DictWriter(fichero,fieldnames=encabezado)
        escritor.writeheader()
        escritor.writerows(productos)

def Creararchivo():
    with open('inventario.csv','w',newline=''):
        print("Fichero creado correctamente")

