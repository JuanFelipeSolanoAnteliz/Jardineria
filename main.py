2


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
import modulos.postProducts as pspr 
import modulos.postPago as pa
import modulos.postPedido as pd
import modulos.postOficnina as ofi
import modulos.postEmpleados as empi
import modulos.postClients as pcli

import json 

def menuProducto():
      while True: 
            os.system("clear")
            print("""
                                                                             _                            _            _            
                                  | |                          | |          | |           
  _ __ ___   ___ _ __  _   _    __| | ___   _ __  _ __ ___   __| |_   _  ___| |_ ___  ___ 
 | '_ ` _ \ / _ \ '_ \| | | |  / _` |/ _ \ | '_ \| '__/ _ \ / _` | | | |/ __| __/ _ \/ __|
 | | | | | |  __/ | | | |_| | | (_| |  __/ | |_) | | | (_) | (_| | |_| | (__| || (_) \__ \
 |_| |_| |_|\___|_| |_|\__,_|  \__,_|\___| | .__/|_|  \___/ \__,_|\__,_|\___|\__\___/|___/
                                           | |                                            
                                           |_|
                  
                  1. Menu de reportes de los productos.
                  2. Actualizar,añadir o eliminar productos.
                  
                    
                  0. SALIR
      """)
            
            opcion = int(input("Ingrese una de las opciones: "))
            if opcion == 1:
                  pr.menu()
            elif opcion == 2:
                 pspr.menu()
                 
def menuPedido():
      while True: 
            os.system("clear")
            

if __name__ == "__main__":

        while True:
                os.system("clear")
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
                    pcli.menu()
                elif(opcion == 2):
                      ofi.menu()
                elif(opcion == 3):
                      empi.menu()
                elif(opcion == 4):
                      pd.menu()
                elif(opcion == 5):
                      pa.menupago()
                elif(opcion == 6):
                      menuProducto()
                elif(opcion == 0):
                      print("Vuelva pronto :D")
                      break


import sys


print(tabulate(pa.getAllPago08Paypal(),tablefmt = 'rounded_grid'))

data = ped.getAllPedidosEntregAtraDeTiemp()
print(data)


import json 


      
