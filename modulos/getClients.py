import storage.cliente as cli 
from tabulate import tabulate


def getAllClientName():
  clientName = list()
  for val in cli.clientes:
    CodigoName = dict({
      "codigo": val.get("codigo_cliente"),
      "nombre": val.get("nombre_cliente")
    })
    clientName.append(CodigoName)
  return clientName

def getAllClientCredCiudad(limiteCredit,ciudad ):
  clienteCredito = []
  for val in cli.clientes:
    if (val.get("limite_credito") >= limiteCredit and val.get("ciudad")):
      clienteCredito.append(val)
  return clienteCredito


def getOneClientCode(codigo):
  for val in cli.clientes:
    if(val.get("codigo_cliente") == codigo):
      return {
          "codigo": val.get("codigo_cliente"),
          "nombre": val.get("nombre_cliente")
      }
    

def getAllSpainClient(spain):
  for val in cli.clientes:
    if(val.get("pais") == spain ):
      return {
        "nombre_cliente": val.get("nombre_cliente"),
        "pais": val.get("pais")
      }
    
def menu():
  print("""
        |  __ \                     | |                | |      | |                | (_)          | |            
        | |__) |___ _ __   ___  _ __| |_ ___  ___    __| | ___  | | ___  ___    ___| |_  ___ _ __ | |_ ___  ___  
        |  _  // _ \ '_ \ / _ \| '__| __/ _ \/ __|  / _` |/ _ \ | |/ _ \/ __|  / __| | |/ _ \ '_ \| __/ _ \/ __| 
        | | \ \  __/ |_) | (_) | |  | ||  __/\__ \ | (_| |  __/ | | (_) \__ \ | (__| | |  __/ | | | ||  __/\__ \ 
        |_|  \_\___| .__/ \___/|_|   \__\___||___/  \__,_|\___| |_|\___/|___/  \___|_|_|\___|_| |_|\__\___||___/ 
                   | |                                                                                           
                   |_|  
        1. obtener todos los clientes (noimbre y codigo)
        2. obtener un cliente por el codigo de cliente (codigo y nombre)
        3.obtener la informacion de un cliente segun el limite de credito y la ciudad (ej: 3000.0 - San Francisco  ) 
""")
  opcion = int(input("\nSeleccone una de las opciones:"))
  if opcion == 1:
    print(tabulate(getAllClientName(), headers = "keys", tablefmt = "rounded_grid"))
  elif opcion == 2:
    int(input("Ingrese el codigo de cliente: "))
    print(tabulate(getOneClientCode(), headers = "keys", tablefmt = "rounded_grid"))
    