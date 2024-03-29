
from tabulate import tabulate
import json 
import requests
def puetsoemp(puesto):
    for val in getAlldataEm():
        if val.get("puesto") == puesto:
            return [val]
            
def getEmpleadoCodigo(codigo):
    for val in getAlldataEm():
        if val.get("codigo_empleado") == codigo:
            return [val]
#json-server storage/empleado.json -b 5506
def getAlldataEm():
    peticion = requests.get(" http://154.38.171.54:5003/empleados")
    data = peticion.json()
    return data
#9
def getAllNamesEmailBoss(codigo):
    nameEmailBoss = []
    for val in getAlldataEm():
        if (val.get("codigo_jefe") == codigo):
             return nameEmailBoss  .append(
                {

                "nombre": val.get("nombre"),
                "apellidos":f'{val.get("apellido1")} {val.get("apellido2")}',
                "email": val.get("email"),
                "jefe": val.get("codigo_jefe")
            }
            )
      

#10
def getAllpuestoNombreApellidoEmailBoss():
    directorGnrl = []
    for val in getAlldataEm():
        if(val.get("codigo_jefe") is None ):   
         return directorGnrl.append({

            "puesto": val.get("puesto"),
            "nombre": val.get("nombre"),
            "apellidos":f'{val.get("apellido1")} {val.get("apellido2")}',
            "email": val.get("email")

        })

    
#11
def getAllNAP():
    noRepresentante = []
    for val in getAlldataEm():
        if(val.get("puesto") != "Representante Ventas" ):
         return noRepresentante.append({
            
            "puesto": val.get("puesto"),
            "nombre": val.get("nombre"),
            "apellidos":f'{val.get("apellido1")} {val.get("apellido2")}'
         })
        
def Deleteidk(id):
    peticion = requests.get(f"http://154.38.171.54:5003/empleados/{id}")
    return [peticion.json()] if peticion.ok else []

    

def menu():
   while True:
    print("""
                                                                   _             _         
                                         _ __ ___ _ __   ___  _ __| |_ ___    __| | ___    
                                        | '__/ _ \ '_ \ / _ \| '__| __/ _ \  / _` |/ _ \   
                                        | | |  __/ |_) | (_) | |  | ||  __/ | (_| |  __/   
                                        |_|  \___| .__/ \___/|_|   \__\___|  \__,_|\___|   
                                         ___ _ _|_|__  _ __ | | ___  __ _  __| | ___  ___ 
                                        / _ \ '_ ` _ \| '_ \| |/ _ \/ _` |/ _` |/ _ \/ __|
                                       |  __/ | | | | | |_) | |  __/ (_| | (_| | (_) \__ !
                                        \___|_| |_| |_| .__/|_|\___|\__,_|\__,_|\___/|___/
                                                    |_|   
          
            1. lista de datos del Jefe (nombre, apellidos, email y cargo) a partir de su codigo. 
            2. Lista con el nombre, apellido e email del director general de la empresa.
            3. lista con los nombres, apellidos y puestos de los empleados que no son Representantes de ventas.
            0.regresar
            
    """)
    

    opcion = int(input("Indique una de las tres opciones: "))
    if opcion == 1:
        codigoJefe = input("indique el codigo del jefe: ")
        print(tabulate(getAllNamesEmailBoss(codigoJefe), headers = "keys", tablefmt = "rounded_grid"))
        input("presione una tecla para continuar...")
    elif opcion == 2:
        print(tabulate(getAllpuestoNombreApellidoEmailBoss(), headers = "keys", tablefmt = "rounded_grid"))
        input("presione una tecla para continuar...")
    elif opcion == 3:
        print(tabulate(getAllNAP(), headers = "keys", tablefmt = "rounded_grid")) 
        input("presione una tecla para continuar...")
    elif opcion == 0:
            
            print("regresando...")
            break
       
        
        

