import json 
import re
import requests
import modulos.getEmpleados as gE 
from tabulate import tabulate
import modulos.getOficina as oF

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
                        
        peticion = requests.post("http://172.16.104.17:5506/empleados", data=json.dumps(empleado, indent=4).encode("UTF-8"))
        res = peticion.json()
        res["Mensaje"] = "Empleado Guardado"
        return [res]

def menu():
    while True:
        os.system("Clear")

     
                     
                