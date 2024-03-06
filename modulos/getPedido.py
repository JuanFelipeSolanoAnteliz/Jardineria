import storage.pedido as ped

def getAlEstado():
    estado = set ()
    for i, val in enumerate (ped.pedido):
        estado.add(val.get("pedido"))
        estado.add(val.get("estado"))    
    return estado     
