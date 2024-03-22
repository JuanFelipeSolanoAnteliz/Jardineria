import json 
import os 
import requests
import re
from tabulate import tabulate
import modulos.getOficina as oF

def postOficina():
    oficina = {}
    while True:
        try:
            if not oficina.get("codigo_oficina"):
                codeOfi = input("Ingrese un codigo de oficina: ")
                if re.match(r'^[A-Z]{3}-[A-Z]{2}',codeOfi) is not None:
                    data = oF.getAllCodigoCiudad()
                    if data:
                        print(tabulate(data, headers="keys", tablefmt= "rounded_grid"))
                    oficina ["codigo_oficina"] = codeOfi    
                else: 
                    raise Exception("El codigo ingresado es valido, recuerde usar unicamente mayusculas y guiunes como separador. (ej: BCN-ES )")
            
            if not oficina.get("ciudad"):
                ciudad = input("Ingrese el nombre de la ciudad: ")      
                if re.match(r'^[A-Z][a-z]+$',ciudad) is not None:
                    oficina["ciudad"] = ciudad
                else: 
                    raise Exception("El nombre ingresado para el espacio (ciudad), no es valido. recuerde iniciar la palabra usando mayusculas.")
                
            if not oficina.get("pais"):
                pais=input("Ingrese el pais donde esta la oficina: ")
                if re.match(r'^[A-Z][a-z]+$',pais) is not None:
                    oficina["pais"] = pais
                else:
                    raise Exception("el pais ingresado no es valido, por favor indicar el nombre iniciando con mayuscula.")
            
            if not oficina.get("region"):
                region = input("Ingrese la region de la oficina")
                if re.macth(r'^[A-Z][a-zA-Z0-9-\s]*$', region) is not None:
                    oficina ["region"] = region
                else: 
                    raise Exception("Region invalida, recuerde usar unicamente letras o guiones (-)")
           
            if not oficina.get("codigo_postal"):
                postal = input("Ingrese el codigo postal")
                if re.match(r'^[0-9]+$',postal) is not None:
                    oficina ["codigo_postal"] = int(postal)
                else:
                    raise Exception("Codigo no valido, recuerde usar unicamente numeros")
            
            if not oficina.get("telefono"):
                telefono = input("""Ingrese un numero telefonico seguido de su indicador de region o prefijo 
                                 telefonico. ( ej: +44 20 78772041 )""")
                if re. match(r'^⁺\d{1,3}\s\d{1,3}\s\d{4,10}$', telefono) is not None:
                    oficina ["telefeono"] = telefono
                else: 
                    raise Exception("numero telefonico invalido, usar solo numerose indicar los respectivos espacios ")
            
            if not oficina.get("linea_direccion1"):
                direccion1 = input("Ingrese la direccion de la oficna")
                oficina ["linea_direccion1"] = direccion1

            if not oficina.get("linea_direccion2"):

                direccion2 = input("Ingrese una segunda direccion: ")
                oficina ["linea_direccion2"] = direccion2
            
            if not oficina.get("id"):
                id = input("Ingrese un ID para su producto: ")
                if re.match(r'^\d',id) is not None:
                    oficina ["id"] = id
                    
        except Exception as error:
                    print(error)
                    
                    
        peticion = requests.post("http://172.16.104.17:5505",  data = json.dumps(oficina,indent=4).encode("UTF-8"))
        rest = peticion.json()
        rest ["Mensaje"] = "pedido guardado"
        return [rest]

def DeleteOficina(id):
    data = oF.DeleteOficinaidk(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5005/oficinas/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Oficina eliminada correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }
    else:
        return {
                "body":[{
                    "Mensaje": "Oficina no encontrado.",
                    "id": id,
            }],
            "status": 400,
            }

def ModificarOficina(id):
    data = oF.DeleteOficinaidk(id)
    if data is None:
            print(f"""

Id de la oficina no encontrado. """)

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
                data[0][datoModificar] = nuevoValor
                break
            else:
                 print(f"""
Seleccion incorrecta""")

        except ValueError as error:
            print(error)

    peticion = requests.put(f"http://154.38.171.54:5005/oficinas/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Oficina Modificado"
    return [res]
    
def menu():
    while True:
        os.system("clear")
        print("""
                __  __                        _               __ _      _                 
                |  \/  |                      | |             / _(_)    (_)                
                | \  / | ___ _ __  _   _    __| | ___    ___ | |_ _  ___ _ _ __   __ _ ___ 
                | |\/| |/ _ \ '_ \| | | |  / _` |/ _ \  / _ \|  _| |/ __| | '_ \ / _` / __|
                | |  | |  __/ | | | |_| | | (_| |  __/ | (_) | | | | (__| | | | | (_| \__ \
                |_|  |_|\___|_| |_|\__,_|  \__,_|\___|  \___/|_| |_|\___|_|_| |_|\__,_|___/
              
              1. Reportes de las oficinas.
              2. Administrador de las oficinas.

              0. salir.
                                                                            
                                                                            
""")
        opcion = input("seleccione una de las opciones: ")
        if opcion == 1: 
                oF.menu()
        elif opcion == 2:
                menuadmin()
        elif opcion == 0:
            break
               

                    
def menuadmin():
    while True:
        print("""
  ____  _                           _     _               _             _           _       _     _                 _                  _                            _            _            
 |  _ \(_)                         (_)   | |             | |           | |         (_)     (_)   | |               | |                | |                          | |          | |           
 | |_) |_  ___ _ ____   _____ _ __  _  __| | ___     __ _| |   __ _  __| |_ __ ___  _ _ __  _ ___| |_ _ __ __ _  __| | ___  _ __    __| | ___   _ __  _ __ ___   __| |_   _  ___| |_ ___  ___ 
 |  _ <| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \   / _` | |  / _` |/ _` | '_ ` _ \| | '_ \| / __| __| '__/ _` |/ _` |/ _ \| '__|  / _` |/ _ \ | '_ \| '__/ _ \ / _` | | | |/ __| __/ _ \/ __|
 | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) | | (_| | | | (_| | (_| | | | | | | | | | | \__ \ |_| | | (_| | (_| | (_) | |    | (_| |  __/ | |_) | | | (_) | (_| | |_| | (__| || (_) \__ \
 |____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/   \__,_|_|  \__,_|\__,_|_| |_| |_|_|_| |_|_|___/\__|_|  \__,_|\__,_|\___/|_|     \__,_|\___| | .__/|_|  \___/ \__,_|\__,_|\___|\__\___/|___/
                                                                                                                                               | |                                            
                                                                                                                                               |_|                                          
                                    
                                1. Agregar oficinas.
                                2. Eliminar una oficina.
                                3. Modificar
                                
                                0. Salir
                                
                                    
              """)


        opcion = int(input("seleccione una opcion"))
        if opcion == 1 :
            print(tabulate(postOficina(), headers = "keys", tablefmt= "rounded_grid" ))
            input("presione una letra para continuar.....")

        elif opcion == 2:
            id = input("Ingrese el id del producto")
            print(tabulate(DeleteOficina(id), headers = "keys", tablefmt= "rounded_grid" ))
            input("presione una letra para continuar.....")
        
        elif opcion == 3:
            id = input("Ingrese el id del producto")
            print(tabulate(ModificarOficina(id), headers = "keys", tablefmt= "rounded_grid" ))
            input("presione una letra para continuar.....")    

            input("presione una tecla para continuar")
        elif opcion == 0:
            break
                
        

                
                
            
    