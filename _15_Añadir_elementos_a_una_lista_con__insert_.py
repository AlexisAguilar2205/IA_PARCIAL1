#31- Añade a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert().
# Tendrás que posicionar 'magenta' en la posición siguiente a la de 'lila' y 'turquesa' en la penúltima posición.
# Deberás hacer esto utilizando posiciones de lista negativa

colore = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#creamos lista colores

colore.insert(-4,'magenta') #añadimos el color con el parametro de la posicion
colore.insert(-1,'turquesa') #añadimos usando numeros negativos

print(colore) #mostramos lista actualizada
