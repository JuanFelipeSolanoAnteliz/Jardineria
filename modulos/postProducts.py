import json
import requests
import modulos.getAllgamas as gG
import os
import re 
import getProducto
import postProducts
from tabulate import tabulate 
#    producto = {
        
#        "codigo_producto": int(input("ingrese un codigo para su producto: ")),
#        "nombre": input("ingrese el nombre del producto a registrar: "),
#        "gama":gG.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
#        "dimensiones": int(input("Ingrese las dimensiones del prodcuto a registrar: ")),
#        "proveedor": input("INgrese el nombre del proovedor: "),
#        "descripcion":input("igngrese una breve descripcion del producto: "),
#        "cantidad_en_stock":int(input("ingrese la cantidad de productos que hay en stock: ")),
#        "precio_proveedor": int(input("Ingrese el precio/valor del producto: " ))
#    }

def getProductoCRUD():
    producto = {}
    while True:
        try:     
        #expresion regular qu evalide cadenas y letras en mayusucula
           if (not producto.get("codigo_producto")):
               codigo = input( "Ingrese un codigo para el producto:  ")
               if(re.match(r'^[A-Z]{2}-[0-9]{3}$',codigo)is not None):
                   data = gG.getProductoCode(codigo)
                   if data:
                       print(tabulate(data, headers = "keys", tablefmt = "rounded_grid"))
                       raise Exception("El codigo ya existe: ")
                   else: 
                        producto ["codigo_producto"] = codigo
                        
               else: 
                    raise Exception("El codigo del producto no cumple con el estandar")
                #expresion regular que valide cada cadena solo letars que las primeras dos sean mayusculas
           if(not producto.get("nombre")):
                nombre = input("ingresa el codigo ")
                if(re.match(r'^[A-Z][0-9]$*\s*)+$',nombre)is not None):
                    producto ["nombre"] = nombre
                    break
                else:
                    raise Exception("El nombre no cumple con las especificaciones ")
            
           if(not producto.get("gama")):
                gama = input("Ingrese una gama para su producto: ")
                if(re.match(r'^[A-Z][a-zA-Z0-9\s.]*$',nombre)) is not None:
                     vgama = gG.getAllNombre(gama)
                     if vgama:
                          producto["gama"]= gama 
                          raise Exception ("gamas validas: Herbaceas, Herramientas, Aromáticas, Frutales, Ornamentales")
                     
           if(not producto.get("dimensiones")):
                dimensiones = input("Ingresa las dimensiones del producto: ")
                if re.match(r'^\d+-\d+$', dimensiones)is not None: 
                     producto ["dimensiones"]== dimensiones
                else:
                     raise Exception ("Dimensiones no vaidas. forma correcta: numero-numero ")
            
           if not producto.get("proveedor"):
                proveedor = input("Ingrese el nombre nombre del proveedor del producto: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\S]+$', proveedor ) is not None:
                     producto ["proveedor"] = proveedor
                else:                                      
                    raise Exception (" El proveedor ingresado no es valido, recuerde que debe escribir iniciando con mayusculas.")
            
           if not producto.get("descripcion"): 
                descripcion =input ("Ingrese una descrpcion para el producto: ")

                producto ["descripcion"] = descripcion
           
           if not producto.get("cantidad_en_stock"):
                stock = input("Ingrese la cantidad de stock del producto: ")
                if re.macth(r'^[0-9]+$', stock ) is not None:
                     stock = int(stock)

                     producto ["cantidad_en_stock"] = stock
                else:                                      
                    raise Exception ("cantidad invalida, recuerde que solo puede indicar nuemros enteros.")

                
           if not producto.gte("precio_venta") :
                precio = input("Ingrese el preicio de venta del producto: ")
                if re.match(r'^[0-9]+$',precio) is not None:
                     precio = int(precio)
                     producto ["precio_venta"] = precio
                else:                                      
                    raise Exception("precio invalido, recuerde que solo puede indicar nuemros enteros.")



           if not producto.get("precio_proveedor"):
                pproveedor = input("Ingrese el precio de proveedor del producto: ")
                if re.match(r'^[0-9]+$',pproveedor) is not None:
                     proveedor = int(pproveedor)
                     producto ["precio_proveedor"] = proveedor
            
                else:                                      
                    raise Exception("precio invalido, recuerde que solo puede indicar nuemros enteros.")
                     
        except Exception as error:
                    print(error)
    
    print(producto)
                            
                                

    peticion = requests.post("http://127.0.0.1:5000", data=json.dumps(producto))
    rest = peticion.json()
    rest["Mensaje"] = "Producto guardado"
    return [rest]

def menu():
    while True:
        os.system("clear")
        print("""
                            *****BIENVENIDO AL ADMINISTRADOR DE PRODUCTOS***** 
                            
                    1. Añadir datos para un nuevo producto.
                    0. regresar
                    
                        
""")    
        
        opcion = int(input("""selccione la opcion numero uno (1) para entrar al 
                           administrador de productos y añadir uno nuevo:  """))
        if opcion == 1:
            print(tabulate(getProductoCRUD(), headers = "keys", tablefmt= "rounded_ grid" ))
        elif opcion == 0:
        
            print("regresando...")
            break