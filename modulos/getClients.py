from tabulate import tabulate
import storage.cliente as cli 
import modulos.getEmpleados as em 
import modulos.getPago as pa


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

#obtener un listado en donde se muestre el nombre de los clientes que son de madrid y que a su vez sus representantes de ventas tengan el codigo 11 y 38

#OBTENER UN LISTADO CON EL NOMBRE DE CADA CLIENTE Y EL NOMBRE Y APELLIDO DE SU REPRESENTANTE DE VENTAS
def getAllclientsYrepventa():
  nombres = []
  for val in cli.cliente:
    for nemp in em.empleados:
      if nemp.get("puesto") == "Representante Ventas" and nemp.get("codigo_empleado") ==  val.get("codigo_empleado_rep_ventas"):
        nombrestbl = {

          "nombre cliente": val.get("nombre_cliente"),
          "Representante de ventas": nemp.get("nombre"),
          "Apellido Rep. ventas": nemp.get("apellido1")

        }
  return nombres.append(nombrestbl)    









#REVISAR MODULOOOOOO








def getAllclientMadrid():
  cliente = []
  for val in cli.clientes:
    for nemp in em.empleados:
      if val.get("region") and val.get("ciudad") == "Madrid" and nemp.get("codigo_empleado") == val.get("codigo_empleado_rep_ventas"):
          
          madrid = {
            "nombre cliente": val.get("nombre_cliente"),
            "ciudad": val.get("region"),
            "codigo representante de ventas": val.get("codigo_empleado_rep_ventas")

          }

  return cliente.append(madrid)

#devolver unn listado en el cual se de el nombre de los clientes que hayan realizado un pago junto con el 
      #nombre de sus representantes
def getNameRepvents():
  clientepago = set ()
  for val in cli.clientes:
    for juan in pa.pago:
      for style in em.empleados:
        if val.get("codigo_cliente") == juan.get("codigo_cliente"):
           clientepago.add(val.get("nombre_cliente"),(juan.get("id_transaccion"),(style.get())))
  return clientepago

      
        

  
    
def menu():
  """
  Muestra un menú con opciones para consultar información de clientes.
  """
  while True:

    print("""
                         ____                       _             _      
                        |  _ \ ___ _ __   ___  _ __| |_ ___    __| | ___ 
                        | |_) / _ \ '_ \ / _ \| '__| __/ _ \  / _` |/ _ !
                        |  _ <  __/ |_) | (_) | |  | ||  __/ | (_| |  __/
                        |_| \_\___| .__/ \___/|_|   \__\___|  \__,_|\___|
                          ___| (_)|_|_ _ __ | |_ ___  ___                
                         / __| | |/ _ \ '_ \| __/ _ \/ __|               
                        | (__| | |  __/ | | | ||  __/\__ \               
                         \___|_|_|\___|_| |_|\__\___||___/       
                    

    
          1. Obtener todos los clientes (nombre y código)
    
          2. Obtener un cliente por el codigo de cliente (codigo y nombre)
    
          3. Obtener la información de un cliente según el límite de crédito y la ciudad (ej: 3000.0 - San Francisco)
    
          4. Obtener la información de los clientes Españoles
    
          5. Obtener la información del cliente según las direcciones del cliente
    
          6. Obtener codigo nombre, codigo portal y codigo de empleado por reporte de venta 
             a partir del codigo postal 
    
          7. Obtener nombre y region del cliente 
    
          8. Obtener los datos del cliente a partir del numero de telefono 

          9. obtener un listado con todos los clientes que sen de madrid y el codigo de su representatnte de ventas
             sea 11 o 38 
    
          10. obtener un listado con los nombres de todos los clientes junto con los nombres
          y apellidos de su representatnte de ventas
    
          0. Salir

    """)

    opcion = int(input("\nSeleccione una de las opciones: "))

    if opcion == 1:
      print(tabulate(getAllClientName(), headers="keys", tablefmt="rounded_grid"))
    elif opcion == 2:
      clientecode = int(input("Ingrese el codigo de cliente: "))
      print(tabulate(getOneClientCode(clientecode), headers="keys", tablefmt="rounded_grid"))
    elif opcion == 3:
      limite = input("Ingrese el limite de credito: ")
      ciudad = input("Ingrese ciudad: ")
      print(
        tabulate(
          getAllClientCredCiudad(limite, ciudad), headers="keys", tablefmt="rounded_grid"
        )
      )
    elif opcion == 4:
      print(tabulate(getAllSpainClient(), headers="keys", tablefmt="rounded_grid"))
    elif opcion == 5:
      direccion_1 = input("Ingrese la direccion principal registrada del cliente: ")
      direccion_2 = input("Ingrese una segunda direccion registrada: ")
      print(
        tabulate(
          getDireccion(direccion_1, direccion_2), headers="keys", tablefmt="rounded_grid"
        )
      )
    elif opcion == 6:
      codigoPostal = input("Ingrese el codigo postal: ")
      print(tabulate(getCodigostal(codigoPostal), headers="keys", tablefmt="rounded_grid"))
    elif opcion == 7:
      print(tabulate(getRegionClients(codigoPostal), headers="keys", tablefmt="rounded_grid"))
    elif opcion == 8:
      telefono = int(input("Ingrese el numero de telefono del cliente: "))
      print(tabulate(getAlldataByTlf(telefono), headers="keys", tablefmt="rounded_grid"))
    
    elif opcion == 9:
      print(tabulate(getAllclientMadrid(), headers = "keys", tablefmt = "rounded_grid" ))
    elif opcion == 10:
      print(tabulate(getAllclientsYrepventa(), headers = "keys", tablefmt = "rounded_grid"))
    elif opcion == 0:
      print("¡Hasta luego!")
      break

if __name__ == "__main__":
  menu()

    