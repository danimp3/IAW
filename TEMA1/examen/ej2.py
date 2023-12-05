num = []
cont= 0
alm = 0
while True:
    num.append(int(input("Introduzca un numero: ")))
    cond = input("Quiere seguir introduciendo numeros? SI/No: ")
    if cond != "si":
        break

numb=int(input("Que numero quiere buscar?: "))  
    
for i in num:
    if i == numb:
        cont = cont+1
        alm=i
print("El numero",alm,"aparece",cont, "veces")