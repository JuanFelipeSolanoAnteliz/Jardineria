import json
import requests




from tabulate import tabulate

def getProductoCode(codigo):
    for val in getAllData():
        if val.get("codigo_producto") == codigo:
            return [val] 



#puerto json-server storage/producto.json -b 5502


def getAllData():
    peticion = requests.get("http://154.38.171.54:5008/productos")
    data = peticion.json
    print(data)

def deleteProductID(id):    
    peticion = requests.get("http://154.38.171.54:5008/productos/{id}")
    return [peticion.json()] if peticion.ok else[]


#decolver un listado con todos los productos que pertenezcan a la gama ornamental
#y que tienen mas de 100 unidades en stock, el listado debera estar por su precio de venta 
#mostrando en primer lugar el mayor precio

def getAllstockPriceGama(gama,stock):
    condiciones = []
    for val in getAllData():
        if val.get("gama") == gama and val.get("cantidad_en_stock") >= stock:
            condiciones.append(val)
            
    def price(val):
        return val.get("precio_venta")
    
    condiciones.sort(key = price,reverse = True)
    for i, val in enumerate(condiciones):
        if(condiciones [i].get("descripcion")):
            condiciones [i]["descripcion"] = f'{condiciones[i]["descripcion"][:5]}...'
    return condiciones
import os


def menu():
    while True:
        os.system("clear")
        print("""
                                                        BIENVENIDO AL MENU DE PRODUCTOS
                                        1.Obtener un producto por su gama y numero de stock.
                                        0.Regresar
                                        
                                        
            
            """)

        opcion = int(input("Seleccione un un a de las dos opciones: "))
        if opcion == 0:
            
            print("regresando...")
            break
        
        elif opcion == 1:
           gama =input("ingrese la gama del producto: ")
           stock =input("indique el stock del producto: ")
                            
           print(tabulate(getAllstockPriceGama(gama,stock), headers= "keys", tablefmt="rounden_grid"))
        elif opcion >= 3:
            print("opcion no existente")

        
        
