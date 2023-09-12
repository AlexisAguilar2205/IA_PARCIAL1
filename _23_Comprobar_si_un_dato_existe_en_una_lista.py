#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

#Haz una tupla que contenga cuatro colores de tu elección. Tendrás que poner una condición con el condicional

# if para cada color que le avise al usuario que el color está en la tupla con un mensaje como este: 

# print('El color rojo está admitido') y una condición False para contemplar cualquier color que no esté en

# la tupla con un mensaje como este: print('Color no admitido'). No puedes utilizar el operador ==. Además

# tendrás que hacer esto con un input() que permita introducir un color al usuario.

color =('negro','morado','purpura','verde') #Se crea la tupla 

color1 = input("Introduzca un color\n") #Solicitamos el color al usuario 

if color1 in color: #Verificamos que el color esta en la tupla 
    print("El color" + color1 + "Esta admitido") #Al verificar que el color este dentro
else:
    print("Color no admitido") #Si no esta se imprimira el si el color introducido 
    