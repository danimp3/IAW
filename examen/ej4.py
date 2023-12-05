lista1 = [0, 5, 8, 4, 3]
lista2 = [8, 6, 2, 1]
nrep = 0
cont= 0

for i in lista1:
    for c in lista2:
        if i == c:
            nrep = 1
        
    
        
if nrep == 1:
    print ("Si existen elementos repetidos en las listas")
else:
    print ("No existen elementos repetidos en las listas")