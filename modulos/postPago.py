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
                    
                    
def DeletePago(id):
    data = gPg.DeleteOficinaidk(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Pago eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }
    else:
        return {
                "body":[{
                    "Mensaje": "Pago no encontrado.",
                    "id": id,
            }],
            "status": 400,
        }

def ModificarPagos(id):
    data = gPg.DeleteOficinaidk(id)
    if data is None:
            print(f"""

Id del pago no encontrado. """)

    while True:
        try:
            print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
            print(f"""
Datos para modificar: """)
            for i, (val, asd) in enumerate(data[0].items()):
                print(f"{i+1}. {val}")

            opcion = int(input(f"""
Seleccione una opción: """))
            datoModificar = list(data[0].keys())[opcion - 1]
            nuevoValor = input(f"""
Ingrese el nuevo valor para {datoModificar}: """)
            if datoModificar in data[0]:
                if data[0][datoModificar] == data[0]["codigo_cliente"] or data[0][datoModificar] == data[0]["total"]:
                    data[0][datoModificar] = int(nuevoValor)
                    
                else:
                    data[0][datoModificar] = nuevoValor
                    
                    break
            else:
                 print(f"""
Seleccion incorrecta""")

        except ValueError as error:
            print(error)

    peticion = requests.put(f"http://154.38.171.54:5006/pagos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Pago Modificado"
    return [res]
def menupago():
    while True:
        
        print("""
              _           _       _     _                 _                  _                                    
     /\      | |         (_)     (_)   | |               | |                | |                                   
    /  \   __| |_ __ ___  _ _ __  _ ___| |_ _ __ __ _  __| | ___  _ __    __| | ___   _ __   __ _  __ _  ___  ___ 
   / /\ \ / _` | '_ ` _ \| | '_ \| / __| __| '__/ _` |/ _` |/ _ \| '__|  / _` |/ _ \ | '_ \ / _` |/ _` |/ _ \/ __|
  / ____ \ (_| | | | | | | | | | | \__ \ |_| | | (_| | (_| | (_) | |    | (_| |  __/ | |_) | (_| | (_| | (_) \__ \
 /_/    \_\__,_|_| |_| |_|_|_| |_|_|___/\__|_|  \__,_|\__,_|\___/|_|     \__,_|\___| | .__/ \__,_|\__, |\___/|___/
                                                                                     | |           __/ |          
                                                                                     |_|          |___/  
                                1. Agregar un nuevo pago
                                2. eliminar pago
                                3. Modificar pago
                                0. salir
              
              """)
        
        opcion = int(input("seleccione una opcion"))
        if opcion == 1 :
            print(tabulate(getpagoCRUD(), headers = "keys", tablefmt= "rounded_grid" ))
            input("presione una letra para continuar.....")

        elif opcion == 2:
            id = input("Ingrese el id del producto")
            print(tabulate(DeletePago(id), headers = "keys", tablefmt= "rounded_grid" ))
            input("presione una letra para continuar.....")
        
        elif opcion == 3:
            id = input("Ingrese el id del producto")
            print(tabulate(ModificarPagos(id), headers = "keys", tablefmt= "rounded_grid" ))
            input("presione una letra para continuar.....")    

            input("presione una tecla para continuar")
        
        

                
                    
        
                
                
                
                    
            
            
                    
                    
                        
                         
                    