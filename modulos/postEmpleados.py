import json 
import re
import requests
import modulos.getEmpleados as gE 
from tabulate import tabulate
import modulos.getOficina as oF
import os

def postEmpleados():
    empleados = {}
    while True:
        try:
            if not empleados.get("codigo_empleado"):
                codigo = input("Ingrese le codigo del empleado: ")
                if re.match(r'^\d{1,2}') is not None:
                    empleados ["codigo_empleado"] = codigo
                    data = gE.getEmpleadoCodigo(codigo)
                    if data:
                         print(tabulate(data, headers="keys", tablefmt= "rounded_grid"))
                         empleados ["codigo_empleado"] = int(codigo)
                         
                    else :
                        raise Exception("este codigo no es valido, recerde usar unicamente numeros enteros.")
            if not empleados.get("nombre"):
                nombre = input("Ingrese el nombre del empleado: ")
                if re.match(r'^[A-Z]{1}[a-z]+$', nombre) is not None:
                    empleados["nombre"] = nombre
                else:
                    raise Exception("El nombre proporcionado no es valido, recuerde inciar en mayusculas. ")
            if not empleados.get("apellido1"):
                apellido1 = input("ingrese el primer apellido: ")
                if re.match(r'^[A-Z]{1}[a-z]+$',apellido1)is not None:
                    empleados["apellido1"] = apellido1
                else:
                    raise Exception("apellido no valido, use solo letras y recuerde iniciar en mayusculas.")
            
            if not empleados.get("apellido2"):
                apellido2= input("Ingrese el segundo apellido: ")
                if re.match(r'^[A-Z]{1}[a-z]+$',apellido2)is not None:
                    empleados["apellido1"] = apellido1
                else:
                    raise Exception("apellido no valido, use solo letras y recuerde iniciar en mayusculas.")
                 
            if not empleados.get("extension"):
                extension = input("Ingrese la extension: ")
                if re.match(r'^[0-9]+$',extension) is not None:
                    empleados ["extensiones"] = extension
                else:
                    raise Exception("la extension es invalida, indique unicamente numeros")
                
            if not empleados.get("email"):
                email = input("ingrese el email del empleado: ")
                if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$',email):
                    empleados ["email"] = email
                
            if not empleados.get("codigo_oficina"):      
                codigofi = input("ingrese el codigo de oficina")
                if re.match(r'^[A-Z]{3}-[A-Z]{2,3}$', codigofi) is not None:
                    empleados ["codigo_oficina"] = codigofi
                else:
                    raise Exception("Codigo no valido, revise que todas las letras esten en mayusculas (ej: SYD-AU )")
            if not empleados.get("codigo_jefe"):
                codeBoss = input("ingrese el codigo de jefe: ")
                if re.match(r'^\d{1,3}+$', codeBoss)is not None:
                    codeBoss =int(codeBoss)
                    empleados ["codigo_jefe"] = codeBoss
                else:
                    raise Exception("El codigo no es valido, verifique que los datso ingresados sean unicamente numericos.")
            
            if not empleados.get("puesto"):
                puesto = input("Ingres el puesto del empleado: ")
                if re.match(r'^[A-Z]{1}[a-z]+$',puesto) is not None:
                    pueto = gE.puetsoemp(puesto)
                    if pueto:
                        
                        empleados ["puesto"] = puesto
                        break
                    raise Exception("Puestos validos: ( Representante Ventas, Subdirector Marketing, Subdirector Ventas, Secretaria, Director Oficina )")
                    
                    # # while True:
                    # #     print("""seleccione un puesto:
                    # #         1. Representante Ventas
                    # #         2. Director Oficina
                    # #         3. Secretaria
                    # #         4. Subdirector Ventas
                    # #         5. Subdirector Marketing
                    # #         6. Director General
                            
                    # #         """)
                    #     opcion = input("seleccione un puesto: ")
                        
                    #     if opcion == 1:
                          
                    
                    
                    
                
        except Exception as error:
                        print(error)           
def DeleteEmpleado(id):
    data = gE.Deleteidk(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5003/empleados/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Empleado eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }
    else:
        return {
                "body":[{
                    "Mensaje": "Empleado no encontrado.",
                    "id": id,
            }],
            "status": 400,
            }

def DeleteEmpleado(id):
    data = gE.Deleteidk(id)
    if data is None:
            print(f"""

Id del empleado no encontrado. """)

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
                if data[0][datoModificar] == data[0]["codigo_cliente"] or data[0][datoModificar] == data[0]["total"]:
                    data[0][datoModificar] = int(nuevoValor)
                    
                else:
                    data[0][datoModificar] = nuevoValor
                    break
            else:
                 print(f"""
Seleccion incorrecta""")

        except ValueError as error:
            print(error)

    peticion = requests.put(f"http://154.38.171.54:5003/empleados/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Empleado Modificado"
    return [res]  
def menu():
    while True:
        os.system("clear")
        print("""
            __  __                        _                             _                _           
            |  \/  |                      | |                           | |              | |          
            | \  / | ___ _ __  _   _    __| | ___    ___ _ __ ___  _ __ | | ___  __ _  __| | ___  ___ 
            | |\/| |/ _ \ '_ \| | | |  / _` |/ _ \  / _ \ '_ ` _ \| '_ \| |/ _ \/ _` |/ _` |/ _ \/ __|
            | |  | |  __/ | | | |_| | | (_| |  __/ |  __/ | | | | | |_) | |  __/ (_| | (_| | (_) \__ \
            |_|  |_|\___|_| |_|\__,_|  \__,_|\___|  \___|_| |_| |_| .__/|_|\___|\__,_|\__,_|\___/|___/
                                                                | |                                 
                                                                |_|                        

              1. reporte de empleados.
              2. administrador de empleados.

              0. Salir      
            """)             

        opcion = input("seleccione una de las opciones: ")
        if opcion == 1: 
                gE.menu()
        elif opcion == 2:
                menuadmin()
        elif opcion == 0:
            break        

def menuadmin():
    while True:
        os.system("Clear")
        print("""
                                 
  ____  _                           _     _               _             _           _       _     _                 _                  _                             _                _           
 |  _ \(_)                         (_)   | |             | |           | |         (_)     (_)   | |               | |                | |                           | |              | |          
 | |_) |_  ___ _ ____   _____ _ __  _  __| | ___     __ _| |   __ _  __| |_ __ ___  _ _ __  _ ___| |_ _ __ __ _  __| | ___  _ __    __| | ___    ___ _ __ ___  _ __ | | ___  __ _  __| | ___  ___ 
 |  _ <| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \   / _` | |  / _` |/ _` | '_ ` _ \| | '_ \| / __| __| '__/ _` |/ _` |/ _ \| '__|  / _` |/ _ \  / _ \ '_ ` _ \| '_ \| |/ _ \/ _` |/ _` |/ _ \/ __|
 | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) | | (_| | | | (_| | (_| | | | | | | | | | | \__ \ |_| | | (_| | (_| | (_) | |    | (_| |  __/ |  __/ | | | | | |_) | |  __/ (_| | (_| | (_) \__ \
 |____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/   \__,_|_|  \__,_|\__,_|_| |_| |_|_|_| |_|_|___/\__|_|  \__,_|\__,_|\___/|_|     \__,_|\___|  \___|_| |_| |_| .__/|_|\___|\__,_|\__,_|\___/|___/
                                                                                                                                                              | |                                 
                                                                                                                                                              |_|                                 

              1. Agregar un empleado.
              2. eliminar un empleado.
              3. Modificar empleado.

              0. Salir

""")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            print(tabulate(postEmpleados(),headers="keys",tablefmt = "rounded_grid"))
        elif opcion == 2:
            id = input("Ingrese el id del producto")
            print(tabulate(DeleteEmpleado(id), headers = "keys", tablefmt= "rounded_grid" ))
            input("presione una letra para continuar.....")
        
        elif opcion == 3:
            id = input("Ingrese el id del producto")
            print(tabulate(DeleteEmpleado(id), headers = "keys", tablefmt= "rounded_grid" ))
            input("presione una letra para continuar.....")    

            input("presione una tecla para continuar")
        elif opcion == 0:
            break

     
                     
                