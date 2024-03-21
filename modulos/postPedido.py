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
        
def DeletePedido(id):
    data = gP.DeletePedidoidk(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5007/pedidos/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Pedido eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }
    else:
        return {
                "body":[{
                    "Mensaje": "Pedido no encontrado.",
                    "id": id,
            }],
            "status": 400,
            }

def ModificarPedido(id):
    data = gP.DeletePedidoidk(id)
    if data is None:
            print(f"""

Id del pedido no encontrado. """)

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
                if datoModificar == "codigo_pedido" or "codigo_cliente":
                    data[0][datoModificar] = int(nuevoValor)
                    break
                else:
                    data[0][datoModificar] = nuevoValor
                    print(tabulate(data[0], headers="keys", tablefmt="rounded_grid"))
                    break
            else:
                 print(f"""
Seleccion incorrecta""")

        except ValueError as error:
            print(error)

    peticion = requests.put(f"http://154.38.171.54:5007/pedidos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Pedido Modificado"
    return [res]




        

def menu():
     while True:
        os.system("clear")
        print("""
              _           _       _     _                 _                  _                                    
     /\      | |         (_)     (_)   | |               | |                | |                                   
    /  \   __| |_ __ ___  _ _ __  _ ___| |_ _ __ __ _  __| | ___  _ __    __| | ___   _ __   __ _  __ _  ___  ___ 
   / /\ \ / _` | '_ ` _ \| | '_ \| / __| __| '__/ _` |/ _` |/ _ \| '__|  / _` |/ _ \ | '_ \ / _` |/ _` |/ _ \/ __|
  / ____ \ (_| | | | | | | | | | | \__ \ |_| | | (_| | (_| | (_) | |    | (_| |  __/ | |_) | (_| | (_| | (_) \__ \
 /_/    \_\__,_|_| |_| |_|_|_| |_|_|___/\__|_|  \__,_|\__,_|\___/|_|     \__,_|\___| | .__/ \__,_|\__, |\___/|___/
                                                                                     | |           __/ |          
                                                                                     |_|          |___/   
                                              1. Registrar un nuevo pedido.
                                              2. Eliminar un pedido.
                                              3. Actualizar un pedido.
                                              
                                              0. salir
                                              
              """)
        opcion = int(input("seleccione una opcion"))
        if opcion == 1 : 
            print(tabulate(getPedidoCRUD(), headers = "keys", tablefmt= "rounded_grid" ))
            input("presione una tecla para continuar")
        elif opcion == 2 :
            id = int(input("Ingrese el id del pedido a eliminar: "))
            print(DeletePedido(id))
            input("presione una tecla para continuar")
        elif opcion == 3:
            id = int(input("Ingrese el id del pedido a modificar: "))
            print(ModificarPedido(id))
            input("presione una tecla para continuar")
        if opcion == 0:
            break
        

