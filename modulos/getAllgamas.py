import json
import requests

def getAllgama():
    peticion = requests. get("http://127.0.0.1:5001")
    peticion.json()

    return peticion.json()


def getAllNombre(gama):
    for val in getAllgama():
        if val.get("gama") == gama:
            return [val]
        
