import json
import requests
import modulos.getProducto as producto
import modulos.getAllgamas as gG


from tabulate import tabulate

def getProductoCode(codigo):
    for val in getAllData():
        if val.get("codigo_producto") == codigo:
            return [val] 



#puerto json-server storage/producto.json -b 5502


def getAllData():
    peticion = requests.get("hhttp://[::1]:5502")
    data = peticion.json
    print(data)

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
def menu():
    while True:
        print("""
                                                        BIENBENIDO AL MENU DE PRODUCTOS
                                        1.Obtener un producto porsu gama y numero de stock.
                                        0.Regresar
                                        
                                        
            
            """)

        opcion = int(input("Seleccione un un a de las dos opciones: "))
        if opcion == 1:
            print(tabulate(getAllstockPriceGama(),headers="keys", tablefmt ="rounded_grid"))
        elif opcion == 0:
            print("regresando")
            print("regresando.")
            print("regresando..")
            print("regresando...")
            break
        
