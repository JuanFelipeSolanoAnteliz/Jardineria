import json
import requests

def getProducto(producto):
    peticion = requests.get("http://127.0.0.1:5000", data=json.dumps(producto))
    rest = peticion.json()
    return rest