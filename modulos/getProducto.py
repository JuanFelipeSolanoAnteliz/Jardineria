import json
import requests




from tabulate import tabulate

def getProductoCode(id):
    peticion = requests.get(f"http://154.38.171.54:5008/productos/{id}")
    return [peticion.json()] if peticion.ok else[]



#puerto json-server storage/producto.json -b 5502


def getAllData():
    peticion = requests.get(f"http://154.38.171.54:5008/productos")
    data = peticion.json()
    return data

def deleteProductID(id):    
    peticion = requests.get(f"http://154.38.171.54:5008/productos/{id}")
    return [peticion.json()] if peticion.ok else[]


#decolver un listado con todos los productos que pertenezcan a la gama ornamental
#y que tienen mas de 100 unidades en stock, el listado debera estar por su precio de venta 
#mostrando en primer lugar el mayor precio

def getAllstockPriceGama(gama,stock):
    condiciones = []
    for val in getAllData():
        if val.get("gama") == gama and (val.get("cantidadEnStock") >= stock):
             condiciones.append(val)
            
    def price(val):
        return val.get("precio_venta")
    
    condiciones.sort(key = price,reverse = True)
    for i, val in enumerate(condiciones):
        # if(condiciones [i].get("descripcion")):
            condiciones [i]= {
                "codigo": val.get("codigo_producto"),
                "venta": val.get("precio_venta"),
                "nombre": val.get("nombre"),
                "gama": val.get("gama"),
                "dimensiones": val.get("dimensiones"),
                "proveedor": val.get("proveedor"),
                "descripcion": f'{val.get("descripcion")[:5]}...' if condiciones[i].get("descripcion") else None,
                "stock": val.get("cantidadEnStock"),
                "base": val.get("precio_proveedor")
            }
            # [i]["descripcion"] = f'{condiciones[i]["descripcion"][:5]}...'
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

        opcion = int(input("Seleccione una de las dos opciones: "))
        if opcion == 0:
            
            print("regresando...")
            break
        
        elif opcion == 1:
           gama =(input("ingrese la gama del producto: "))
           stock =int(input("indique el stock del producto: "))                  
           print(tabulate(getAllstockPriceGama(gama,stock), headers= "keys", tablefmt="rounden_grid"))
           input("Seleccioneuna teclapara continuar: ")
        elif opcion >= 3:
            print("opcion no existente")

        
        
