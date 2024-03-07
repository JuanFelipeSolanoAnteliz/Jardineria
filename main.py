from tabulate import tabulate

import modulos.getClients as clientes
import modulos.getOficina as of 
import modulos.getEmpleados as em 
import modulos.getPedido as ped 

print(tabulate(ped.getAllPedRechazado2009(),tablefmt = 'rounded_grid'))

#data = ped.getAllPedidosEntregAtraDeTiemp()
#print(data)

