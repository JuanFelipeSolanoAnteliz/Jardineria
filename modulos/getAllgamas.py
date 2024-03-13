import json
import requests

def getAllgama():
    peticion = requests. get("http://127.0.0.1:5001")
    data = peticion.json()

    return data


def getAllNombre(): 
    gamaNombre = []
    for val in getAllgama:
        