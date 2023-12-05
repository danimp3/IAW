creditos = {'Matematicas':6,'Fisica':4,'Quimica':5}

for i in creditos:
    print(i,"tiene", creditos.get(i), "creditos")
    
    totCred= creditos.get('Matematicas') + creditos.get('Fisica') + creditos.get('Quimica')
print("Total de creditos:", totCred)