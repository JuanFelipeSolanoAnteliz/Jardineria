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

