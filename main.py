#from tabulate import tabulate

import modulos.getClients as clientes
import modulos.getOficina as of 
import modulos.getEmpleados as em 
import modulos.getPedido as ped 
import modulos.getPago as pa 

def menu():
    print(f"""
  _    _                    _____      _            _             _
 |  \/  |                  |  __ \    (_)          (_)           | |
 | \  / | ___ _ __  _   _  | |__) | __ _ _ __   ___ _ _ __   __ _| |
 | |\/| |/ _ \ '_ \| | | | |  ___/ '__| | '_ \ / __| | '_ \ / _` | |
 | |  | |  __/ | | | |_| | | |   | |  | | | | | (__| | |_) | (_| | |
 |_|  |_|\___|_|_|_|\__,_| |_|   |_|  |_|_| |_|\___|_| .__/ \__,_|_|
          

                1. cliente
                2. oficina
                3. empleados
                4. pedidos
                5. pagos
    """)
    
menu()
    
opcion = int(input("\nSeleccone una de las opciones:"))
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


#import sys

#for nombre, objeto in sys.modules.items():
#    if nombre.startswith("modulos"):
#        modulo = getattr(objeto,"__name__", None)
#        if(modulo != "modules"):
#            file = modulo.split("get")[-1]
#            print(modulo)

#print(tabulate(pa.getAllPago08Paypal(),tablefmt = 'rounded_grid'))

#data = ped.getAllPedidosEntregAtraDeTiemp()
#print(data)

#recuerde siempre poner autoguardado o dar crt+s
