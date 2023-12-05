frutas = {'platano': 1.35, 'manzana': 0.8, 'pera': 0.85, 'naranja':0.7}

frutsol = input("Que fruta va a comprar: ")
kg = int(input("cuantos kg quiere: "))

if frutsol in frutas:
 
  print("El precio total es de:",frutas.get(frutsol)*kg)
else:
        print("La fruta solicitada no se encuentra")