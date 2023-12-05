alumnos = {}
cont = 1
numal = int(input("cuantos alumnos va a introducir: "))


while cont <= numal:
   alum= input("Introduzca el nombre del alumno: ")
   notas =[]
   while True:
       notasol = int(input("Introduzca las notas: "))
       if notasol <= -1:
           break
       else:
           notas.append(notasol)
   
   
   media=sum(notas) / len(notas)
   
   alumnos[alum] = media
   cont= cont+1
   
print(alumnos)
