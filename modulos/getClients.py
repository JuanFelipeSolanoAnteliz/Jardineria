from tabulate import tabulate
import storage.cliente as cli 


#1
def getAllClientName():
  clientName = list()
  for val in cli.clientes:
    CodigoName = dict({
      "codigo": val.get("codigo_cliente"),
      "nombre": val.get("nombre_cliente")
    })
    clientName.append(CodigoName)
  return clientName


#2
def getOneClientCode(codigo):
  for val in cli.clientes:
    if(val.get("codigo_cliente") == codigo):
      return {
          "codigo": val.get("codigo_cliente"),
          "nombre": val.get("nombre_cliente")
      }
#3    
def getAllClientCredCiudad(limiteCredit,ciudad ):
  clienteCredito = []
  for val in cli.clientes:
    if (val.get("limite_credito") >= limiteCredit and val.get("ciudad") == ciudad):
      clienteCredito.append({
        
        "codigo": val.get("codigo_cliente"),
        "nombre": val.get("nombre_cliente"),
        "contacto": val.get("nombre_contacto"),
        "apellido": val.get("apellido_contacto"),
        "telefono": val.get("telefono"),
        "fax": val.get("fax"),
        "Direccion1_": val.get("linea_direccion1"),
        "Direccion2": val.get("linea_direccion2"),
        "ciudad": val.get("ciudad"),
        "region": val.get("region"),
        "pais":val.get("pais"),
        "codigo_postal": val.get("codigo_postal"),
        "reporte_ventas_clientes": val.get("codigo_empleado_rep_ventas"),
        "limite_credito": val.get("limite_credito")  
      })
  return clienteCredito

#4
def getAllSpainClient(spain):
  for val in cli.clientes:
    if(val.get("pais") == spain ):
      return ({
        "nombre_cliente": val.get("nombre_cliente"),
        "pais": val.get("pais")
      })
 #5     
def getDireccion(direccion,direccion2):
  for val in cli.clientes:
    if (val.get("linea_direccion1") == direccion) and (val.get("linea_direccion2")== direccion2):
      return ({
      "nombre": val.get("nombre_cliente"),
      "direccion":val.get("linea_direccion1"),
      "direccion2": val.get("linea_direccion2")
    })
      

  
    
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
        3. obtener la informacion de un cliente segun el limite de credito y la ciudad (ej: 3000.0 - San Francisco)
        4. obtener la informacion de los clientes Españoles
        5. obtener la informacion del cliente segun las direcciones del cliente
""")
  opcion = int(input("\nSeleccone una de las opciones:"))
  if opcion == 1:
    print(tabulate(getAllClientName(), headers = "keys", tablefmt = "rounded_grid"))
  elif opcion == 2:
    print(tabulate(getOneClientCode(), headers = "keys", tablefmt = "rounded_grid"))
  elif opcion == 3:
    print(tabulate(getAllClientCredCiudad(), headers = "keys", tablefmt = "rounded_grid"))
    print()
  elif opcion == 4:
    print(tabulate(getAllSpainClient(),headers = "keys", tablefmt = "rounded_grid"))