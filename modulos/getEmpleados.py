import storage.empleado as em 

#9
def getAllNamesEmailBoss(codigo):
    nameEmailBoss = []
    for val in em.empleados:
        if (val.get("codigo_jefe") == codigo):
             nameEmailBoss.append(
                {

                "nombre": val.get("nombre"),
                "apellidos":f'{val.get("apellido1")} {val.get("apellido2")}',
                "email": val.get("email"),
                "jefe": val.get("codigo_jefe")
            }
            )
    return nameEmailBoss    
#10
def getAllpuestoNombreApellidoEmailJefe(puesto):
    puestoEmailJefe = []
    for val in em.empleados:
        if(val.get("puesto") == puesto ):   
         puestoEmailJefe.append({

            "puesto": val.get("puesto"),
            "nombre": val.get("nombre"),
            "apellidos":f'{val.get("apellido1")} {val.get("apellido2")}',
            "email": val.get("email")

        })

    return puestoEmailJefe
#11
def getAllNAP(rVentas):
    noRepresentante = []
   
    for val in em.empleados:
        if(val.get("puesto") != (rVentas) ):
         noRepresentante.append({
            
            "puesto": val.get("puesto"),
            "nombre": val.get("nombre"),
            "apellidos":f'{val.get("apellido1")} {val.get("apellido2")}'
         })

    return noRepresentante


