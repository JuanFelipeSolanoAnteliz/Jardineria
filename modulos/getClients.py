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
#2 obtener la informacin de un cliente a partir del codigo de cliente 
def getOneClientCode(codigo):
  codigClient = []
  for val in cli.clientes:
    if(val.get("codigo_cliente") == codigo):
       nombreycodigo= {
          "codigo": val.get("codigo_cliente"),
          "nombre": val.get("nombre_cliente")
      }    
    codigClient.append(nombreycodigo)   
  return  codigClient
  
#3  obtener todos los datos de los clientes a partir de su limite de credito y la ciudad 
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
#4 obtener todos el nombre de los clientes esoañoles y su nacionalidad 
def getAllSpainClient():
    nameSpain = []
    for val in cli.clientes:
      if(val.get("pais") == "spain" ):
        dictName = ({
        "nombre_cliente": val.get("nombre_cliente"),
        "pais": val.get("pais")
      })
    return nameSpain.append(dictName)
#5 obtener la info del cliente a partir de cualquiera de las dos direcciones
#que tiene cada cliente
def getDireccion(direccion,direccion2):
  apellidoCli= []
  for val in cli.clientes:
    if (val.get("linea_direccion1") == direccion) or (val.get("linea_direccion2")== direccion2):
      infMostrada = {
        
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
    }
    apellidoCli.append(infMostrada)
  return apellidoCli
#6 obtener codigo nombre, codigo portal y codigo de empleado por reporte de venta 
# a partir del codigo postal 
def getCodigostal(codePostal):
  for val in cli.clientes:
    if (val.get("codigo_postal") == codePostal) :
      return {
        "nombre": val.get("nombre_cliente"),
        "codigo Postal": val.get("codigo_postal"),
        "reporte de ventas": val.get("codigo_empleado_rep_ventas")

      }
    
#7 obtener nombre y region del cliente 
def getRegionClients():
    regionCli = []
    for val in cli.clientes:
        if val.get("region") is not None:
            regionCli.append({
                "nombre": val.get("nombre_cliente"),
                "region": val.get("region")
            })
    return regionCli
#8 obtener los datos del cliente a partir del numero de telefono      
def getAlldataByTlf(telefono):
  numtelefono = []
  for val in cli.clientes:
    if val.get("telefono") == telefono:
      dataCli = {
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
    }
  return numtelefono.append(dataCli)

  
    
def menu():
  print("""
         _____                       _                  _        _                  _ _            _                     
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
        6. obtener codigo nombre, codigo portal y codigo de empleado por reporte de venta 
           a partir del codigo postal 
        7. obtener nombre y region del cliente 
        8. obtener los datos del cliente a partir del numero de telefono  
""")
  menu()

  opcion = int(input("\nSeleccone una de las opciones:"))
  if opcion == 1:
    print(tabulate(getAllClientName(), headers = "keys", tablefmt = "rounded_grid"))
  elif opcion == 2:
    clientecode = int(input("Ingrese el codigo de cliente: "))
    print(tabulate(getOneClientCode(clientecode), headers = "keys", tablefmt = "rounded_grid"))
  elif opcion == 3:
    limite = input("ingrese el limite de credito: ")
    ciudad = input("Ingrese ciudad: ")
    print(tabulate(getAllClientCredCiudad(limite,ciudad), headers = "keys", tablefmt = "rounded_grid"))
  elif opcion == 4:
    print(tabulate(getAllSpainClient(),headers = "keys", tablefmt = "rounded_grid"))
  
  elif opcion == 5:
    direccion_1 = input("Ingrese la direccion principal registrada del cliente: ")
    direccion_2 = input("Ingrese una segunda direccion registrada: ")
    print(tabulate(getDireccion(direccion_1,direccion_2),headers = "keys", tablefmt = "rounded_grid"))
  
  elif opcion == 6:
    codigoPostal = input("Ingrese el codigo postal: ")
    print(tabulate(getCodigostal(codigoPostal),headers = "keys", tablefmt = "rounded_grid"))
  
  elif opcion == 7:
    print(tabulate(getRegionClients(codigoPostal),headers = "keys", tablefmt = "rounded_grid"))

  elif opcion == 8:
    telefono = int("Ingrese el numero de telefono del cliente:")
    print(tabulate(getAlldataByTlf(telefono), headers = "keys", tablefmt = "rounded_grid"))
    

    