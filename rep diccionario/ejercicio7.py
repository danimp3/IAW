cesta = {}
total = 0

while True:
    key = input("Que quieres agregar?: ")
    valor = input("Introduzca el valor: ")
    cesta [key] = valor
    mas=input('¿quieres introducir algo mas?: ')
    
    if mas == 'no':
        for i in cesta:
           total = int(cesta.get(i)) + total
           print(i)
        break
    elif mas != 'no':
            print("ERROR, introduzca si o no")
            break
print("Total:",total)


