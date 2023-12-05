monedas = {'Euro':'€', 'Dollar':'$','Yen':'Y'}

tipMon =input("Dime el tipo de moneda: ")

if tipMon in monedas:
    print("el tipo de moneda es ",monedas.get(tipMon))
else:
    print("ERROR, tipo de moneda no valida")