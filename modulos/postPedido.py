import json
import modulos.getPedido as gP
import requests
import os
import re
from tabulate import tabulate
import modulos.getClients as gC




def getPedidoCRUD():

    pedido = {} 

    while True:
        try:
            if not pedido.get("codigo_pedido"):
                codigo = (input("Ingrese el codigo del producto: "))

                if re.match(r'^[0-9]+$', codigo) is not None:
                    codigo = int(codigo)
                    data = gP.getCodigoPedido(codigo)
                    if data:
                        print(tabulate(data, headers = "keys", tablefmt = "rounded_grid"))
                        raise Exception("el codigo ingresado ya fue registrado.")
                    else: 
                        pedido  ["codigo_pedido"] = codigo 
                else:
                    raise Exception("codigo no valido.")
            
            if not(pedido.get("fecha_pedido")):
                fecha = input("Ingrese la fecha en la que se realizo el pedido (ej: 2000-01-20 ): ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$',fecha) is not None:
                    pedido ["fecha_pedido"] = fecha
                else:
                    raise Exception("fecha invalida, use el formato año-dia-mes solo con caracteres numericos.")
                

            if not(pedido.get("fecha_esperada")):
                fechaesp = input("Ingrese la fecha de entrega estima para el pedido: ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$',fechaesp) is not None:
                    pedido ["fecha_esperada"] = fechaesp
                else:
                      raise Exception("fecha invalida, use el formato año-dia-mes solo con caracteres numericos.")
                
            if not(pedido.get("fecha_entrega")):
                fechaentr = input("Ingrese la fecha en la que fue entregado el pedido: ")
                if fechaentr.strip().lower() == "none" :
                    pedido  ["fecha_entrega"] == None

                if re.match(r'^\d{4}-\d{2}-\d{2}$',fechaentr) is not None:
                    pedido  ["fecha_entrega"] == fechaentr

                else:
                      raise Exception("fecha invalida, use el formato año-dia-mes solo con caracteres numericos.")
                
            if not(pedido.get("estado")):
                estado = input("Ingrese el estadodel producto: ")
                if re.match(r'^[A-Z][a-z]+$', estado ) is not None:
                     estadoped = gP.getAlEstado(estado)
                     if estadoped:
                          pedido["estado"] = estado
                     else:
                          raise Exception("Estados validos : Entregado / Rechazado / Pendiente")
            if not(pedido.get("comentario")):
                 comentarios = input("Ingrese un comentario a cerca del pedido: ")
                 
                 pedido ["comentario"] == comentarios

            if not (pedido.get("codigo_cliente")):
                 codigocli = input( "Ingrese el codigo de cliente: ")
                 if re.match(r'^[0-9]+$',codigocli) is not None:
                     codigo = int(codigo)
                     codigo = gC.getOneClientCode(codigo)
                     if codigocli:
                         codigocli ["codigo_cliente"] = codigo 
                         print(tabulate(codigocli, headers = "keys", tablefmt = "rounded_grid"))
                     raise Exception("codigo invalido, recuerde que solo puede usar numeros enteros.")
                    
        except Exception as error:
                    print(error)



        peticion = requests.post("http://172.16.104.17:5503",  data = json.dumps(pedido))
        rest = peticion.json()
        rest ["Mensaje"] = "pedido guardado"
        return [rest]
    
def menu():
     while True:
        os.system("clear")
        print("""
                                              ******BIENVENIDO AL ADMINISTRADOR DE PEIDOS******
                                              1. Registrar un nuevo pedido.
                                              
                                              0. salir
                                              
              """)
        opcion = int(input("seleccione una opcion"))
        if opcion == 1 : 
            print(tabulate(getPedidoCRUD(), headers = "keys", tablefmt= "rounded_grid" ))
        if opcion == 0:
            break
        

