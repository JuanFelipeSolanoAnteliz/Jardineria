import json
import re
import requests
from tabulate import tabulate
import modulos.getClients as gc

def postclient():
    cliente = {}
    while True:
        os.system("clear")
        try:

            if not cliente.get("codigo_cliente"):
                code = input("Ingrese el codfio del cliente: ")
                if re.match(r'^\d+$',code) is not None:
                    code = int(code)
                    cliente ["codigo_cliente"] = code
                    data = gc.getcodeClie(code)
                if data:
                         print(tabulate(data, headers="keys", tablefmt= "rounded_grid"))
                         cliente ["codigo_empleado"] = int(code)
            if not cliente.get("nombre_cliente"):
                nombreCli = input("Ingrese el nombre del cliente: ")
                if re.match(r'^[A-Z]{1}[a-z]+\s[A-Z][a-z]+$',nombreCli)is not None:
                      cliente ["nombre_cliente"] = nombreCli 
                else: 
                     raise Exception("El nombre indicado es invalido, recuerde usar unicamente letras e iniciar en mayusculas.")
            
            if not cliente.get("nombre_contacto"):
                nombreCon = input("Ingrese el nombre de contacto del cliente: ")
                if re.match(r'^[A-Z]{1}[a-z]+\s[A-Z][a-z]+$',nombreCon) is not None:
                    cliente["nombre_contacto"] = nombreCon
                else:
                     raise Exception("El nombre indicado es invalido, recuerde usar unicamente letras e iniciar en mayusculas.")
            
            if not cliente.get("apellido_contacto"):
                apellido = input("ingrese el appelido del cliente: ")
                if re.match(r'^[A-Z]{1}[a-z]+$',apellido) is not None:
                    cliente ["apellido_contacto"] = apellido
                else: 
                     raise Exception("El apellido no es valido, recuerde ingresar solo un apellido e iniciar en mayuscula.")
            if not cliente.get("telefono"):
                telefono = input("Ingrese el numero de telefono del cliente: ")
                if re.match(r'^\d+$',telefono) is not None:
                      cliente ["telefono"] = telefono
                else:
                     raise Exception("telefono invalido, recuerde no usar espacion ni prefijos telefonicos como (+57, +44...)")    
            if not cliente.get("fax"):
                fax= input("Ingrese el Fax del cliente: ")
                if re.match(r'^\d+$',fax) is not None:
                      cliente ["fax"] = fax
                else:
                     raise Exception("El dato ingresado no es valido, recuerde usar unicamente numeros sin espacios entre ellos.")
            
            if not cliente.get("linea_direccion1"):
                direc1 = input("Ingrese la direccion del cliente: ")
                if re.match(r'^\d*-?[a-zA-Z]+(?:[^\w\s]?[a-zA-Z]+)*$',direc1) is not None:
                    cliente ["linea_direccion1"]  = direc1
            
            if not cliente.get("linea_direccion2"):
                direc2 = input("ingrese una segunda direccion: ") 
                if re.match(r'^\d*(-[a-zA-Z]+(?:[^\w\s]?[a-zA-Z]+)*)?$',direc2) is not None:
                     cliente ["linea_direccion2"] = direc2
            
            if not cliente.get("ciudad") :
                ciudad = input("ingrese la ciudad: ")
                if re.match(r'^[A-Z]{1}[a-z]+$',ciudad) is not None:
                     cliente ["ciudad"] = ciudad
                else:
                     raise Exception("Ciudad no valida, recuerde inicar en mayusculas.")
            
            if not cliente.get("region"):
                region = input("Ingrese la region del cliente: ")
                if region and re.match(r'^([A-Z]{1}[a-z]+)?$',region)is not None:
                             cliente["region"] = region
            
            if not cliente.get("pais"):
                pais = input("ingrese el pais del cliente: ")
                if re.match(r'^[A-Z]+[a-z]*$',pais) is not None:
                     cliente ["pais"] = pais
                else:
                     raise Exception("pais no valido, recuerde siempre iniciar en mayusculas.")
            
            if not cliente.get("limite_credito"):
                 limite= input("ingrese el limite de credito del cliente: ")
                 if re.match(r'^\d+.*\d*',limite) is not None:
                      pais = int(pais)
                      cliente ["limite_credito"] = pais
                 else: 
                      raise Exception("el dato proporcionado no es valido, recuerde usar unicamente numeros")
            break
def DeleteClientes(id):
    data = gc.DeleteClienteCodigoasd(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5001/cliente/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Cliente eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }
    else:
        return {
                "body":[{
                    "Mensaje": "Cliente no encontrado.",
                    "id": id,
            }],
            "status": 400,
            }

def ModificarCliente(id):
    data = data = gc.DeleteClienteCodigoasd(id)
    if data is None:
            print(f"""

Id del Cliente no encontrado. """)

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
                if datoModificar == "codigo_empleado_rep_ventas" or "codigo_cliente" or "limite_credito":
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

            peticion = requests.put(f"http://154.38.171.54:5001/cliente/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
            res = peticion.json()
            res["Mensaje"] = "Cliente Modificado"
            return [res]

        except Exception as error:
            print(error)
import os
def menu():
     while True:
          os.system("clear")
          print("""             ******BIENVENIDO AL ADMINISTRADOR DE CLIENTES******
                
                1. Agregar un nuevo cliente.

                0. Salir

""")
          
          opcion = int(input("ingrese una opcion: "))
          if opcion == 1:
               print()
          elif opcion == 0:
               break
        
               
        
                


