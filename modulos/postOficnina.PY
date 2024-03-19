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

            
                
        

                
                
            
    