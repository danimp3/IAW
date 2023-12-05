
datos = {}

while True:
    key = input("Que quieres agregar?: ")
    valor = input("Introduzca el valor: ")
    datos [key] = valor
    print (datos)
    mas=input('¿quieres introducir algo mas?: ')
    
    if mas == 'no':
        break