notas = []
cont = 0
totn= 0

while cont < 5:
  notas.append(int(input("Introduce las notas:")))
  cont = cont+1

for i in notas:
    totn=i+totn


media= totn/len(notas)
print("notas:",notas, "media:",media, "maxima:", max(notas),"minima:",min(notas))




