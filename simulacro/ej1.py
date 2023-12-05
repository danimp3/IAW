dic = []
p =[]
while True:
    dic.append(input("Introduce una palabra:"))  
    sino = input("Quiere introducir otra? SI/NO: ")
    if sino != 'si':
        break
    
 
for i in dic:
    p.append(len(i))

print (max(p), i)