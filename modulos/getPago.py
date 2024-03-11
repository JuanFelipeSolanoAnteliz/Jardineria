import storage.pago as pa
#14
def getAllPago08Paypal():
    formaPago = []
    for val in pa.pago:
        año = val.get("fecha_pago")
        if val.get("forma_pago") == "PayPal":
            if año.startswith("2008"):
                formaPago.append({
                    "codigo_cliente": val.get("codigo_cliente"),
                    "fecha_pago": val.get("fecha_pago"),
                    "forma_pago": val.get("forma_pago")
                })
    return formaPago

def getAllpagosPaypal():
    paypal = []
    for val in pa.pagos:
        if val.get("forma_pago") == "paypal":
            datapagos = {

            "codigo": val.get("codigo_cliente"),
            "forma_pago": val.get("forma_pago"),
            "id_transaccion": val.get("id_transaccion"),
            "fecha": val.get("fecha_pago"),
            "total": val.get("total")
            } 
    return paypal.append(datapagos)

def getAllFormaPago():
    formaDePago =[]
    formaPagoRep = set()
    for val in pa.pagos:
        if val.get("forma_pago") not in formaPagoRep:
            formaDePago.append({"forma_pago": val.get("forma_pago")})
            formaPagoRep.add(val.get("forma_pago"))
            
    return formaDePago

def menu():
    print(""" 
                            Reporte de pagos
          1. lista de pagos realizados con paypal en 2008
          2. lista de pagos realizados con paypal 
          3. obtener una lista de formas de pagos
""")

