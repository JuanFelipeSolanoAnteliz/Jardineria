import json 
import requests
from tabulate import tabulate
import requests

def getAlldata():
    peticion = requests.get("http://172.16.104.17:5503")
    data =peticion.json 
    print(data)
#15
def getAlEstado():
    estado = set ()
    for i, val in enumerate: getAlldata()
    estado.add(val.get("codigo_pedido"))
    estado.add(val.get("estado"))    
    return estado     

#from datetime import datetime

#def getAllPedidosEntregAtraDeTiemp():
#      pedidosEntregado = set()
#         if (val.get("estado") == "entregado" and val.get("fecha_entrega"))is None:
#               val["fecha_entrega"] = val.get("fecha_esperada")
#          if val.get("estado") == "entregado":
#               date1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
#              start = datetime.strptime(date1, "%d/%m/%Y")
#              end = datetime.strptime(date2, "%d/%m/%Y")
#              diff = end.date() - start.date()
#              if(diff.day < 0):
#                  pedidosEntregado.append({
#                     "codigo_de_pedido":val.get("codigo_pedido"),
#                      "codigo_de_cliente":val.get("codigo_cliente"),
#                      "fecha_esperada": val.get("fecha_esperada"),
#                      "fecha_de_entrega": val.get("fecha_entrega")
#             })
    #return pedidosEntregado        

from datetime import datetime
#from tabulate import tabulate

#def getAllPedidosEntregAtraDeTiemp():
#    pedidosEntregado = []
#    for val in ped.pedido:
#        if (val.get("estado") == "entregado" and val.get("fecha_entrega")) is None:
#            val["fecha_entrega"] = val.get("fecha_esperada")
#        if val.get("estado") == "entregado":
#            date1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
#            date2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
#            start = datetime.strptime(date1, "%d/%m/%Y")
#            end = datetime.strptime(date2, "%d/%m/%Y")
#            diff = (end - start).days
#            if diff < 0:
#                pedidosEntregado.append({
#                    "codigo_de_pedido": val.get("codigo_pedido"),
#                    "codigo_de_cliente": val.get("codigo_cliente"),
#                    "fecha_esperada": val.get("fecha_esperada"),
#                    "fecha_de_entrega": val.get("fecha_entrega")
#                })
#       return pedidosEntregado
#15
def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = list()
    for val in getAlldata():
        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") == None):
            val["fecha_entrega"] = val.get("fecha_esperada")
        if (val.get("estado") == "Entregado"):
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if diff.days < 0:
                pedidosEntregado.append({
                    "codigo_de_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega")
                })
    return pedidosEntregado
#16
def getAllCodigoPedDosantesDiasFechaespera():
    pedidoAdelantado = list()

    for val in getAlldata():
        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") == None):
            val["fecha_entrega"] = val.get("fecha_esperada")
        if (val.get("estado") == "Entregado"):
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if diff.days  >= 2 :
                pedidoAdelantado.append({
                    "codigo_de_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega")
                })
    return pedidoAdelantado
#17
def getAllPedRechazado2009():
    pedidoRechazado = []
    for val in getAlldata():
        año = val.get("fecha_entrega")
        if (val.get("estado") == "Rechazado" and val.get("fecha_entrega") is not None): 
            if año.startswith("2009"):
                pedidoRechazado.append ({
                    "codigo_pedido": val.get("codigo_pedido"),
                    "estado_pedido": val.get("estado"),
                    "fecha_entrega": val.get("fecha_entrega")
                })
            
    return pedidoRechazado
#18
def getAllpepdiosEnero():
    pedidoEnero = []
    for val in getAlldata():
      
        if val.get("fecha_entrega") != None and val.get("estado") == "Entregado":
            fechaentrega = "/".join(val.get("fecha_entrega").split("-")[::-1])
            start = datetime.strptime(fechaentrega,"%d/%m/%Y" )
            if val.get("estado") == "Entregado" and start.month == 1:
                pedidoEnero.append(val)

    return pedidoEnero

def menu():
    while True:
        print("""
                                             ____                       _             _      
                                            |  _ \ ___ _ __   ___  _ __| |_ ___    __| | ___ 
                                            | |_) / _ \ '_ \ / _ \| '__| __/ _ \  / _` |/ _ !
                                            |  _ <  __/ |_) | (_) | |  | ||  __/ | (_| |  __/
                                            |_| \_\___| .__/_\___/|_|   \__\___|  \__,_|\___|
                                             _ __   __|_|__| (_) __| | ___  ___              
                                            | '_ \ / _ \/ _` | |/ _` |/ _ \/ __|             
                                            | |_) |  __/ (_| | | (_| | (_) \__ \             
                                            | .__/ \___|\__,_|_|\__,_|\___/|___/             
                                            |_|                                      


            1. Obtener el pedido y el codigo de pedido
            2. Obtener los pedidos entregados fuera de fecha (atrasados)
            3. obetener los pedidos entregados antes de la fecha esperada
            4. Obtener el codigo, estado y fecha de entrega de lo spedidos rechazados en el año 2009
            5. Obtener todos los pedidos entregados en el mes de enero 
            0. regresar
    """)
        
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            print(tabulate(getAlEstado(), headers = "keys", tablefmt = "rounded_grid"))

        elif opcion == 2:
            print(tabulate(getAllPedidosEntregadosAtrasadosDeTiempo(), headers = "keys", tablefmt = "rounded_grid"))

        elif opcion == 3: 
            print(tabulate(getAllCodigoPedDosantesDiasFechaespera(), headers = "keys", tablefmt = "rounded_grid"))
        
        elif opcion == 4:
            print(tabulate(getAllPedRechazado2009(), headers = "keys", tablefmt = "rounded_grid"))

        elif opcion == 5: 
            print(tabulate(getAllpepdiosEnero(), headers = "keys", tablefmt = "rounded_grid"))
        elif opcion == 0:
           
            print("regresando...")
            
        
    
            break

       