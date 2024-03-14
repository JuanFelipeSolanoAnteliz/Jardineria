import json
import requests
import modulos.getAllgamas as gG
import os



def getProductoCRUD():
    producto = {

        "codigo_producto": int(input("ingrese un codigo para su producto: ")),
        "nombre": input("ingrese el nombre del producto a registrar: "),
        "gama":gG.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
        "dimensiones": int(input("Ingrese las dimensiones del prodcuto a registrar: ")),
        "proveedor": input("INgrese el nombre del proovedor: "),
        "descripcion":input("igngrese una breve descripcion del producto: "),
        "cantidad_en_stock":int(input("ingrese la cantidad de productos que hay en stock: ")),
        "precio_proveedor": int(input("Ingrese el precio/valor del producto: " ))

}

    peticion = requests.post("http://127.0.0.1:5000", data=json.dumps(producto))
    rest = peticion.json()
    rest["Mensaje"] = "Producto guardado"
    return [rest]

def menu():
    while True:
        os.system("clear")
        print("""
                            *****BIENVENIDO AL ADMINISTRADOR DE PRODUCTOS***** 
                            
""")    