from tabulate import tabulate

import modulos.getClients as clientes
import modulos.getOficina as of 
import modulos.getEmpleados as em 

print (tabulate(em.getAllNAP("Representante Ventas")))