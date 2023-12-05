facturas = {}
total_fact= 0
fact_cob= 0
print("Eliga una opcion:")
print("1. Crear facturas")
print("2. Pagar factura")
print("3. Terminar")

opci = int(input("Elige una opcion: "))

while True: 
        if opci == 1:
            nuevFact = int(input("Introduzca el numero de la nueva factura: "))
            costFact = int(input("Introduzca el coste de la nueva factura: "))
            facturas [nuevFact] = costFact
            total_fact= costFact + total_fact
        elif opci == 2:
            numFact = int(input("Introduzca el numero de factura a pagar: "))
            fact_cob = fact_cob + facturas.get(numFact)
            total_fact= total_fact - facturas.get(numFact)
            facturas.pop(numFact)
        elif opci == 3:
            print("Terminando programa....")
            break
        else:
            print("opcion incorrecta")
            
        print("Actualmente hay", total_fact,"euros pendientes de cobro")
        print("Actualmente hay", fact_cob,"euros cobrados")
    
        opc = input("¿Quiere realizar otra operacion?: ")
        if opc == "no":
            print("Terminando programa....")
            break
        elif opc != "si":
            print("Error escriba si o no")
            break
        else:
            print("Eliga una opcion:")
            print("1. Crear facturas")
            print("2. Pagar factura")
            print("3. Terminar")

            opci = int(input("Elige una opcion: "))


