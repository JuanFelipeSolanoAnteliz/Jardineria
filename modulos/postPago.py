import json 
import requests
from tabulate import tabulate
import modulos.getPago as gPg
import os 
import modulos.getClients as cli
import modulos.getProducto as gP
import re

def getpagoCRUD():
    pago = {}
    while True:
        try:
            if not pago.get("codigo_producto"):
                codigoClie = input("Ingrese el codigo del cliente: ")
                if re.match(r'^[0-9]+$')