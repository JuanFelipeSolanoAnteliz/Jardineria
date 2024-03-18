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
                    oficina ["codigo_oficina"] = codeOfi
                    
                else: 
                    raise Exception("El codigo ingresado es valido, recuerde usar unicamente mayusculas y guiunes como separador. (ej: BCN-ES )")
            if not oficina.get("ciudad"):
                ciudad = input("Ingrese el nombre de la ciudad: ")      
                if re.match(r'^[A-Z][a-z]+$',ciudad) is not None:
                    oficina["ciudad"] = ciudad
                else: 
                    raise Exception("El nombre ingresado para el espacio (ciudad), no es valido. recuerde iniciar la palabra usando mayusculas."):
                
            if not oficina.get("pais"):
                pais=input("Ingrese el pais donde esta la oficina: ")
                if re.match(r'^[A-Z][a-z]+$',pais) is not None:
                    oficina["pais"] = pais
                else:
                    raise Exception("el pais ingresado no es valido, por favor indicar el nombre iniciando con mayuscula.")
                
                
            
    