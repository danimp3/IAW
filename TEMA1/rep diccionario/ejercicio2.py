nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
direc = input("Dime tu direccion: ")
telefono = input("Dime tu telefono: ")
datos = {}
datos["nombr"] = nombre
datos["edade"] = edad
datos["dire"] = direc
datos["Tlfo"] = telefono

print(datos.get("nombr"), "tiene", datos.get("edade"), "años, vive en", datos.get("dire"), "y su numero de telefono es", datos.get("tfono"))