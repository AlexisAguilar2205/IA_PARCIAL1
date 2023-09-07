#Elimina de la siguiente lista los elementos 'lila' y 'marron'
#Solo puedes eliminarlos utilizando el metodo remove()

color = ['rojo', 'azul','verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

#declara lista 

c1 = color.pop (0) #eliminamos el amarillo 
c2 = color.pop (-6) #eliminamos el marron 

print(color,"\n")
print(c1,c2)#corroboramos que se hayan eliminado los elementos 


