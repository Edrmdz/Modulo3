#Programa Reto semana 10
#permite crear 2 listas de distintas logitudes
#longitud y elementos son especificados por el usuario
#que imprima las listas originales
#que imprima la primera lista indicando que se han eliminado los elementos que estan tambien en la lista 2

def agregando_datos(lista, valor):   # funcion para crear listas a partir de datos ingresados
    lista.append(valor)
    return lista


colores1 = []
colores2 = []
long1 = int(input("Numero de colores de la 1er lista : ")) #ingresar datos para crear lista 1
for i in range(long1):
    color = input(f'Color {i + 1}? ')
    colores1 = agregando_datos(colores1, color)
print (f'la lista de colores 1 es {colores1}')

long2 = int(input("Numero de colores de la 2da lista : ")) #ingresar datos para crear lista 2
for i in range(long2):
    color2 = input(f'Color {i + 1}? ')
    colores2 = agregando_datos(colores2, color2)
print (f'la lista de colores 2 es {colores2}')

a =set(colores1)                                # convirtiendo listas para crear lista que elimina comunes con lsita 2.
b = set(colores2)
diff = (a) - (b)
print(f'La lista1 sin los colores comonues de la lista 2 es ', (diff))


