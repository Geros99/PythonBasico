nombres = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo: (M o F) ")
if sexo == "M":
    if nombres.lower() < "M":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombres.lower() > "N":
        grupo = "A"
    else:
        grupo = "B"        
print ("Usted pertenece al grupo " + grupo)