import storage.producto as pr 
from tabulate import tabulate

#decolver un listado con todos los productos que pertenezcan a la gama ornamental
#y que tienen mas de 100 unidades en stock, el listado debera estar por su precio de venta 
#mostrando en primer lugar el mayor precio

def getAllstockPriceGama(gama,stock):
    condiciones = []
    for val in pr.productos:
        if val.get("gama") == gama and val.get("cantidad_en_stock") >= stock:
            condiciones.append(val)
            
    def price(val):
        return val.get("precio_venta")
    
    condiciones.sort(key = price,reverse = True)
    for i, val in enumerate(condiciones):
        if(condiciones [i].get("descripcion")):
            condiciones [i]["descripcion"] = f'{condiciones[i]["descripcion"][:5]}...'
    return condiciones
