
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

#Completa el siguiente fragmento de c�digo:
#def colores(*args):
#	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco est� mal.')

#colores()

def colores(*args):
	print("El color", args[1], 'es mi favorito.', 'El color', args[0], "tampoco est� mal.")

colores("negro","azul") #a�adimos los parametros faltantes de la funcion

#################################################################################################
#Crea una funci�n que realice la suma de cinco n�meros utilizando solo *args. 
#Debes imprimir el resultado en la consola. La suma no se realizar� directamente sobre el print().

def suma(*args): #definimos la funcion con args para no especificar cantidad exacta de parametros
	total = 0#creamos variable que almacene el total de la suma (igualada a cero para que comience ahi la suma)
	for x in args: #ciclo que se repetira tantas veces como parametros tengamos
		total = total + x #suma el parametro con lo anterior ya acumulado
	print("La suma de los numeros es: ",total) #sale del for e imprime la suma

suma(5,10,15,20,25) #mandamos llamar a funcion y le mandamos los parametros