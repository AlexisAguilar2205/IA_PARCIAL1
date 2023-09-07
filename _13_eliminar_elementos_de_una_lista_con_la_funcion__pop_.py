#Elimina de la siguiente lista los elementos 'negro' y 'azul' utilizando el metodo pop().
#Ademas, tendras que guardar esos dos colores en una nueva lista.

color = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

val1 = color.pop (0) #Eliminamos de la lista el color rojo y lo guardamos en una variable
val2 = color.pop (-2) #Eliminamos de la lista el color blanco.

print(color) #comprobamos que se haya wliminado 

val3 = [val1, val2] #creamos la nueva lista con estos dos valores

print(val3) # imprimimos la nueva lista 