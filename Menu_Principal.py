import funciones
import os

if not os.path.exists("inventario.csv"):
    funciones.Creararchivo()



opc = 0
while(opc != 5):
    print(".:Menu:.")
    print("1- Agregar inventario nuevo\n2- Modificar producto\n3- Venta\n4- Mostrar producto existente\n5- Salir")
    opc = int(input("Selecciona una opcion nueva: "))
    if (opc == 1):
        funciones.AgregarProductoNuevo()
    if (opc == 2):
        funciones.ModificarStock()
    if (opc == 3):
        funciones.venta()
    if (opc == 4):
        funciones.MostrarProducto()
    if (opc == 5):
        print("salir")

