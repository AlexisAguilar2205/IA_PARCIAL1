#31- A�ade a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert().
# Tendr�s que posicionar 'magenta' en la posici�n siguiente a la de 'lila' y 'turquesa' en la pen�ltima posici�n.
# Deber�s hacer esto utilizando posiciones de lista negativa

colore = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#creamos lista colores

colore.insert(-4,'magenta') #a�adimos el color con el parametro de la posicion
colore.insert(-1,'turquesa') #a�adimos usando numeros negativos

print(colore) #mostramos lista actualizada
