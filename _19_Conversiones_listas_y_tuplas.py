#Convierte la siguiente lista en una tupla y asegúrate que se haya convertido en tupla correctamente
# imprimiendo en la consola el tipo de elemento que es.

marcas = ['bmw', 'ford', 'mercedes', 'nissan', 'lexus', 'toyota', 'kia', 'honda', 'vw', 'audi']
#creamos lista llamada colores

tupla = tuple(marcas) #convertimos lista a tupla
print(type(tupla))#imprimimos el tipo de dato para verificar la conversion
