import storage.pedido as ped

def getAlEstado():
    estado = set ()
    for i, val in enumerate (ped.pedido):
        estado.add(val.get("pedido"))
        estado.add(val.get("estado"))    
    return estado     

#from datetime import datetime

#def getAllPedidosEntregAtraDeTiemp():
 #   pedidosEntregado = set()
  #     if (val.get("estado") == "entregado" and val.get("fecha_entrega"))is None:
   #          val["fecha_entrega"] = val.get("fecha_esperada")
    #    if val.get("estado") == "entregado":
     #        date1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
      ##      start = datetime.strptime(date1, "%d/%m/%Y")
        #     end = datetime.strptime(date2, "%d/%m/%Y")
         #    diff = end.date() - start.date()
          #   if(diff.day < 0):
           #     pedidosEntregado.append({
            #        "codigo_de_pedido":val.get("codigo_pedido"),
             #       "codigo_de_cliente":val.get("codigo_cliente"),
              #      "fecha_esperada": val.get("fecha_esperada"),
               #     "fecha_de_entrega": val.get("fecha_entrega")
             #})
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

def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = list()
    for val in ped.pedido:
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

def getAllCodigoPedDosantesDiasFechaespera():
    pedidoAdelantado = list()

    for val in ped.pedido:
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

def getAllPedRechazado2009():
    pedidoRechazado = []
    for val in ped.pedido:
        año = val.get("fecha_entrega")
        if (val.get("estado") == "Rechazado" and val.get("fecha_entrega") is not None): 
            if año.startswith("2009"):
                pedidoRechazado.append ({
                    "codigo_pedido": val.get("codigo_pedido"),
                    "estado_pedido": val.get("estado"),
                    "fecha_entrega": val.get("fecha_entrega")
                })
            
    return pedidoRechazado

def getAllpepdiosEnero():
    pedidoEnero = []
    for val in ped.pedido:
      
        if val.get("fecha_entrega") != None and val.get("estado") == "Entregado":
            fechaentrega = "/".join(val.get("fecha_entrega").split("-")[::-1])
            start = datetime.strptime(fechaentrega,"%d/%m/%Y" )
            if val.get("estado") == "Entregado" and start.month == 1:
                pedidoEnero.append(val)

    return pedidoEnero