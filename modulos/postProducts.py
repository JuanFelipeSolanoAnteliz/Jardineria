import json
import requests
import modulos.getAllgamas as gg
import os
import re 
import modulos.getProducto as pr

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
        os.system("clear")
        try:     
        #expresion regular qu evalide cadenas y letras en mayusucula
               if not producto.get("codigo_producto"):
                    codigo = input( "Ingrese un codigo para el producto:  ")
               if re.match(r'^([A-Z]{2})-([0-9]{3})$', codigo) is not None:
                    data = pr.getProductoCode(codigo)
                    if data:
                         print(tabulate(data, headers = "keys", tablefmt = "rounded_grid"))
                         raise Exception("El codigo ya existe: ")
                    else: 
                         producto ["codigo_producto"] = codigo
                         
               else: 
                    raise Exception("El codigo del producto no cumple con el estandar")
                    #expresion regular que valide cada cadena solo letars que las primeras dos sean mayusculas
               if(not producto.get("nombre")):
                    nombre = input("ingresa el nombre: ")
                    if(re.match(r'^[A-Z][a-zA-Z0-9\s.]*$',nombre))is not None:
                         producto ["nombre"] = nombre
                    
               else:
                    raise Exception("El nombre no cumple con las especificaciones ")

               if(not producto.get("gama")):
                    gama = input("Ingrese una gama para su producto: ")
                    if(re.match(r'^[A-Z][a-zA-Z0-9\s.]*$',gama)) is not None: 
                              producto["gama"]= gama 
                    else:
                         raise Exception ("gamas validas: Herbaceas, Herramientas, Aromáticas, Frutales, Ornamentales")
                         
               if(not producto.get("dimensiones")):
                    dimensiones = input("Ingresa las dimensiones del producto: ")
                    if re.match(r'^\d+-\d+$', dimensiones)is not None: 
                         producto ["dimensiones"] = dimensiones
                    else:
                         raise Exception ("Dimensiones no validas. forma correcta: numero-numero ")

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
                    stock = int(input("Ingrese la cantidad de stock del producto: "))
                    if re.macth(r'^[0-9]+$', stock ) is not None:
                       

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

    
                            
                                

        peticion = requests.post("http://154.38.171.54:5008/productos", data=json.dumps(producto,indent=4).encode("UTF-8"))
        rest = peticion.json()
        rest["Mensaje"] = "Producto guardado"
        return [rest]

def deleteProducto(id):
    datos = pr.getProductoCode(id)  # Suponiendo que pr.getProductoCode obtiene los detalles del producto

    if datos:  # Comprueba si existen datos del producto
        peticion = requests.delete(f"http://154.38.171.54:5008/productos/{id}")
        if peticion.status_code == 200:  # Comprueba si la eliminación fue exitosa (204: Sin contenido)
            datos.append({"mensaje": "Producto eliminado correctamente"})  # Agrega mensaje de éxito
            return {
                "body": datos,
                "id": id,
                "estado": "exito"  # Indica eliminación exitosa
            }
        else:
            return {
                "body": datos,
                "id": id,
                "estado": "error",  # Indica error durante la eliminación
                "mensaje": f"Error al eliminar producto: {peticion.status_code}"  # Incluye código de error
            }
    else:
        return {
            "body": [],  # No se encontraron datos del producto
            "id": id,
            "estado": "error",  # Indica error
            "mensaje": f"Producto con ID {id} no encontrado"  # Mensaje de error informativo
        }

          
def modificarProducto(id):
    data = pr.deleteProductID(id)
    if data is None:
            print("""

Id del producto no encontrado. """)

    while True:
        try:
            print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
            print("""
Datos para modificar: """)
            for i, (val, idk) in enumerate(data[0].items()):
                print(f"{i+1}. {val}")

            opcion = int(input("""
Seleccione una opción: """))
            datoModificar = list(data[0].keys())[opcion - 1]
            nuevoValor = input(f"""
Ingrese el nuevo valor para {datoModificar}: """)
            if datoModificar in data[0]:
                if datoModificar != "cantidadEnStock" or "precio_venta" or "precio_proveedor":
                    data[0][datoModificar] = (nuevoValor)
                    break
                else:
                    data[0][datoModificar] = int(nuevoValor)
                    print(tabulate(data[0], headers="keys", tablefmt="rounded_grid"))
                    break
            else:
                 print("""
Seleccion incorrecta""")

        except ValueError as error:
            print(error)

  

def menu():
    while True:
        os.system("clear")
        print("""
                                          _           _       _     _                 _                  _                            _            _            
     /\      | |         (_)     (_)   | |               | |                | |                          | |          | |           
    /  \   __| |_ __ ___  _ _ __  _ ___| |_ _ __ __ _  __| | ___  _ __    __| | ___   _ __  _ __ ___   __| |_   _  ___| |_ ___  ___ 
   / /\ \ / _` | '_ ` _ \| | '_ \| / __| __| '__/ _` |/ _` |/ _ \| '__|  / _` |/ _ \ | '_ \| '__/ _ \ / _` | | | |/ __| __/ _ \/ __|
  / ____ \ (_| | | | | | | | | | | \__ \ |_| | | (_| | (_| | (_) | |    | (_| |  __/ | |_) | | | (_) | (_| | |_| | (__| || (_) \__ \
 /_/    \_\__,_|_| |_| |_|_|_| |_|_|___/\__|_|  \__,_|\__,_|\___/|_|     \__,_|\___| | .__/|_|  \___/ \__,_|\__,_|\___|\__\___/|___/
                                                                                     | |                                            
                                                                                     |_|                                            
                            
                    1. Añadir datos para un nuevo producto.
                    2. Eliminar un producto.
                    3. Modificar un producto.
                    
                    0. regresar
                    
                        
""")    
        
        opcion = int(input("""selccione una opcion.  """))
     
       

        if opcion == 1:
               print(tabulate(getProductoCRUD(), headers = "keys", tablefmt= "rounded_ grid" ))
               input("Presione un atecla para continuar...")
        elif opcion == 2:
               id=input("Ingrese el ID del producto que desea eliminar:")
               print(tabulate(deleteProducto(id), headers = "keys", tablefmt= "rounded_ grid" ))
               input("Presione un atecla para continuar ...")
        elif opcion == 3:
               id=input("Ingrese el ID del producto que desea modificar:")
               print(tabulate(modificarProducto(id), headers = "keys", tablefmt= "rounded_ grid" ))
        elif opcion == 0:
          
               print("regresando...")
               break