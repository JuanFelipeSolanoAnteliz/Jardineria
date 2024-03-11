import storage.oficina as of
from tabulate import tabulate

#12 obtener codigo y ciudad de la oficina
def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            "codigo": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    return codigoCiudad
#13 obtener el la ciudad, telefono y oficinas de un pais en especifico
def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in of.oficina:
        if (val.get("pais") == pais):
            ciudadTelefono.append({
                "ciudad": val.get("ciudad"),
                "telefono": val.get("telefono"),
                "oficinas" : val.get("cpodigo_oficina"),
                "pais" : val.get("pais") 
            })
    return ciudadTelefono

def menu():
    print("""
                                Reporte de oficina
          
          1. obtener codigo y ciudad de la oficina.
          2. obtener el la ciudad, telefono y oficinas de un pais en especifico.

""")
    
    menu()

    opcion = int(input("seleccione una opcion de las presentes en el indice: "))
    if opcion == 1: 
        print(tabulate(getAllCodigoCiudad(),headers = "keys", tablefmt = "rounded_grid"))
    elif opcion == 2:
        pais = input("Ingrese un pais: ")
        print(tabulate(getAllCiudadTelefono(pais), headres ="keys", tablefmt = "rounded_grid"))

