import json 
import requests

from tabulate import tabulate
#puerto: json-server storage/oficina.json -b 5505

def getAllcodeOfi():
    codigof = []
    for val in getAlldataOf():
        return codigof.append({
            
        "codigo de oficina": val.get("codigo_oficina")
        })
    
    
def getAlldataOf():
    peticion = requests.get("http://172.16.104.17:5505")
    data= peticion.json()
    print(data)
#12 obtener codigo y ciudad de la oficina

 
def getAllCodigoCiudad():
    codigoCiudad = []
    for val in getAlldataOf():
        return codigoCiudad.append({
            "codigo": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    
#13 obtener el la ciudad, telefono y oficinas de un pais en especifico
def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in getAlldataOf():
        if (val.get("pais") == pais):
            return ciudadTelefono.append({
                "ciudad": val.get("ciudad"),
                "telefono": val.get("telefono"),
                "oficinas" : val.get("cpodigo_oficina"),
                "pais" : val.get("pais") 
            })
def DeleteOficinaidk(id):
    peticion = requests.get(f"http://154.38.171.54:5005/oficinas/{id}")
    return [peticion.json()] if peticion.ok else []


def menu():
    while True:
        print("""
                                     ____                       _             _      
                                    |  _ \ ___ _ __   ___  _ __| |_ ___    __| | ___ 
                                    | |_) / _ \ '_ \ / _ \| '__| __/ _ \  / _` |/ _ !
                                    |  _ <  __/ |_) | (_) | |  | ||  __/ | (_| |  __/
                                    |_| \_\___| .__/ \___/|_|   \__\___|  \__,_|\___|
                                            __|_|     _                              
                                     ___  / _(_) ___(_)_ __   __ _                  
                                    / _ \| |_| |/ __| | '_ \ / _` |                 
                                   | (_) |  _| | (__| | | | | (_| |                 
                                    \___/|_| |_|\___|_|_| |_|\__,_|                 
            
            1. obtener codigo y ciudad de la oficina.
            2. obtener el la ciudad, telefono y oficinas de un pais en especifico.
            0.regresar

    """)
        
        

        opcion = int(input("seleccione una opcion de las presentes en el indice: "))
        if opcion == 0: 
            break
        elif opcion == 1: 
            print(tabulate(getAllCodigoCiudad(),headers = "keys", tablefmt = "rounded_grid"))
        elif opcion == 2:
            pais = input("Ingrese un pais: ")
            print(tabulate(getAllCiudadTelefono(pais), headres ="keys", tablefmt = "rounded_grid"))
        
            
            break
               

