adivinaNumero= 33
intento = 0
while True:
    numsoli= int(input("Introduzca un numero: "))
    if numsoli == adivinaNumero:
        intento = intento +1
        print("Has acertado el numero, te ha llevado", intento, "intentos")
        break
    elif numsoli < adivinaNumero:
        intento = intento +1
        print("El numero introducido es menor que el que tienes que adivinar")
    elif numsoli > adivinaNumero:
            intento = intento +1
            print("El numero introducido es mayor que el que tienes que adivinar")