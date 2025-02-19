import csv
import os

productos = list()

def AgregarProductoNuevo():
    opc = 0
    productos.clear()
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
    productos.clear()
    with open('inventario.csv','r',newline='') as fichero:
        lector = csv.DictReader(fichero)
        for linea in lector:
            productos.append(linea)
    return productos

def ModificarStock():
    i=1
    stock = LeerStock()
    for linea in stock:
        print(f'{i}-{linea}')
        i+=1
    modificar = int(input("Que elemento deseas modificar"))
    if modificar <= len(stock):
        diccionario = stock[modificar-1]
        opc = int(input("Que deseas modificar:\n1-nombre\n2-stock\n3-precio\n"))
        if opc == 1:
            diccionario['nombre']=input('nuevo nombre: ')
            print(diccionario)
        elif opc == 2:
            diccionario['stock']=input('nuevo numero de piezas: ')
            print(diccionario)
        elif opc == 3:
            diccionario['precio']=input('nuevo precio: ')
            print(diccionario)
        else:
            print('opcion no valida')
        stock[modificar-1]=diccionario
        SobreEscribir(stock)

def SobreEscribir(nueva_lista):
    if os.path.exists('inventario.csv'):
        with open('inventario.csv','w',newline='') as fichero:
            encabezado = ['nombre','stock','precio']
            escritor = csv.DictWriter(fichero,fieldnames=encabezado)
            escritor.writeheader()
            escritor.writerows(nueva_lista)

def venta():
    i=1
    stock = LeerStock()
    print('Que producto se vendio')
    for producto in stock:
        print(f"{i}- {producto['nombre']}")
        i+=1
    opc = int(input('Que producto se vendio: '))
    if opc <= len(stock):
        diccionario = stock[opc-1]
        venta = int(input(f"Cuantos {diccionario['nombre']} se vendieron: "))
        stock_viejo = diccionario['stock']
        stock_viejo = int(stock_viejo)
        if stock_viejo-venta >= 0 :
            diccionario['stock'] = stock_viejo-venta
            SobreEscribir(stock)
            print(f'Quedan {stock_viejo-venta} {diccionario['nombre']}')
    else:
        print('opcion no valida')
    
def MostrarProducto():
    inventario = LeerStock()
    for producto in inventario:
        print(producto)
    productos.clear()
