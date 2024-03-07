from tabulate import tabulate

import modulos.getClients as clientes
import modulos.getOficina as of 
import modulos.getEmpleados as em 
import modulos.getPedido as ped 
import modulos.getPago as pa 

print(tabulate(pa.getAllPago08Paypal(),tablefmt = 'rounded_grid'))

#data = ped.getAllPedidosEntregAtraDeTiemp()
#print(data)

#recuerde siempre poner autoguardado o dar crt+s
