import json 
import requests
from tabulate import tabulate
import modulos.getPago as gPg
import os 
import modulos.getClients as cli
import modulos.getProducto as gP
import re

def getpagoCRUD():
    pago = {}
    while True:
        try:
            if not pago.get("codigo_producto"):
                codigoClie = input("Ingrese el codigo del cliente: ")
                if re.match(r'^[0-9]+$', codigoClie) is not None:
                    codigoClie = int(codigoClie)
                    data = gP.getProductoCode(codigoClie)
                    if data:
                        print(tabulate(data, headers="keys", tablefmt= "rounded_grid"))
                        raise Exception("codigo ya existente")
                else: 
                    pago ["codigo_producto"] = codigoClie
            else: 
                raise Exception("codigo no valido recuerde usar unicamente numero enteros")
            
            if not pago.get("forma_pago"):
                formapago =input("Ingrese el metodo de pago del pedido: ")
                if re.match(r'^[A-Z]+$',formapago)is not None:
                    pago ["forma_pago"] = formapago
                else:
                    raise Exception("""metodo de pago no encontrado. Formas de pago validas: PayPal, Cheque, Transferencia.""")
            if not pago.get("id_transaccion"):
                idpago = input("Ingrese el ID de la transaccion: ")   
                if re.match(r'^[a-z]{2}-[a-z]{3}-\d{6}$',idpago)is not None:
                    pago ["id_transaccion"] = idpago
                else:
                    raise Exception("ID no valido, por favor rectifique e intente de nuevo.")
            
            if not pago.get("fecha_pago"):
                fecha = input("Ingrese la fecha del pago: ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$', fecha) is not None:
                    pago ["fecha_pago"] = fecha
                    
                else:
                    raise Exception("fecha no valida. verifique si esta usando el formato año-mes-dia (ej: 2000-11-24)")
            
            if not pago.get("total"):
                total =input("ingres el valor correspondiente al total: ")
                if re.match(r'^[0-9]+$',total) is not None:
                    total ["total"] = total
                    
                else: 
                    raise Exception("Dato invalido, recuerde ingresar unicamente datos numericos enteros.")
        
        except Exception as error:
                    print(error)
                    
                    
        peticion = requests.post("http://172.16.104.17:5503",  data = json.dumps(pago,indent=4).encode("UTF-8"))
        rest = peticion.json()
        rest ["Mensaje"] = "pedido guardado"
        return [rest]
            
def menu():
    while True:
        
        print("""
                                ****BIENVENDO AL ADMINISTRADOR DE PAGOS****
                                1. Agregar un nuevo pago
                                
                                0.
              
              """)
        

                
                    
        
                
                
                
                    
            
            
                    
                    
                        
                         
                    