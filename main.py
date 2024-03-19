import os
#la libreria OS se importa en cada modulo debajo del "True del While en cada"
#from tabulate import tabulate
from tabulate import tabulate
import modulos.getClients as clientes
import modulos.getOficina as of 
import modulos.getEmpleados as em 
import modulos.getPedido as ped 
import modulos.getPago as pa 
import modulos.getProducto as pr

def menuProducto():
      while True: 
            os.system("clear")
            print("""
                                          ********* BIENVENIDO AL MENU  *********
                  1. Menu de reportes de los productos.
                  2. Actualizar,añadir o eliminar productos.
                  
                    
                  0. SALIR
      """)
            
            opcion = int(input("Ingrese una de las opciones: "))
            if opcion == 1:
                  print (tabulate())

if __name__ == "__main__":

        while True:
                print(f"""
                 _    _                    _____      _            _             _
                |  \/  |                  |  __ \    (_)          (_)           | |
                | \  / | ___ _ __  _   _  | |__) | __ _ _ __   ___ _ _ __   __ _| |
                | |\/| |/ _ \ '_ \| | | | |  ___/ '__| | '_ \ / __| | '_ \ / _` | |
                | |  | |  __/ | | | |_| | | |   | |  | | | | | (__| | |_) | (_| | |
                |_|  |_|\___|_|_|_|\__,_| |_|   |_|  |_|_| |_|\___|_| .__/ \__,_|_|
                                                                    !_!
                                                                     
                                1. cliente
                                2. oficina
                                3. empleados
                                4. pedidos
                                5. pagos
                                6. productos 
                      
                                0. salir
                """)
                

                
                opcion = int(input("¡Bienvendo! Seleccone una de las opciones:"))
                if(opcion == 1):
                    clientes.menu()
                elif(opcion == 2):
                      of.menu()
                elif(opcion == 3):
                      em.menu()
                elif(opcion == 4):
                      ped.menu()
                elif(opcion == 5):
                      pa.menu()
                elif(opcion == 6):
                      menuProducto()
                elif(opcion == 0):
                      print("Vuelva pronto :D")
                      break


import sys

for nombre, objeto in sys.modules.items():
   if nombre.startswith("modulos"):
       modulo = getattr(objeto,"__name__", None)
       if(modulo != "modules"):
           file = modulo.split("get")[-1]
           print(modulo)

print(tabulate(pa.getAllPago08Paypal(),tablefmt = 'rounded_grid'))

data = ped.getAllPedidosEntregAtraDeTiemp()
print(data)


import json 

with open("storage/cliente.json", "r") as f:
    fichero = f.read()
    data = json.loads(fichero)
    for i, val in enumerate(data):
        data[i]["id"] = (i+1)
    data = json.dumps(data, indent=4).encode("utf-8")
    with open("storage/cliente.json", "wb+") as f1:
        f1.write(data)
        f1.close()
      
"http://154.38.171.54:5001"