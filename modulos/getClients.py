import storage.cliente as cli 
def getAllClientName():
  clientName = list()
  for val in cli.clientes:
    CodigoName = dict({
      "codigo_cliente": val.get("codigo_cliente"),
      "nombre_cliente": val.get("nombre_cliente")
    })
    clientName.append(CodigoName)
  return clientName

def getOneClientCode(codigo):
  for val in cli.clientes:
    if(val.get("codigo_cliente") == codigo):
      return {
          "codigo_cliente": val.get("codigo_cliente"),
          "nombre_cliente": val.get("nombre_cliente")
      }
    
