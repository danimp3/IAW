fech = input("dame una fecha DD/MM/AAAA: ")
diaf = fech[0:2]
mesf = fech[3:5]
anof = fech[6:10]

meses = {'01':'Enero','02':'Febrero','03':'Marzo','04':'Abril','05':'Mayo','06':'Junio','07':'Julio','08':'Agosto','09':'Septiembre','10':'Octubre','11':'Noviembre','12':'Diciembre'}

print(diaf,"de", meses.get(mesf),"de", anof)
