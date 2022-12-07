
'''
Escribe un programa en Python que modifique la lista mares siguiendo el orden siguiente:

1. Cambia a la vez los valores de los elementos undécimo y duodécimo de la lista mares por los
valores 'del norte' y 'alborán'. Muestra la lista mares
2. En la lista mares, inserta un elemento más con el valor 'báltico'. Muestra la lista mares
3. Borra el quinto elemento de la lista mares. Muestra la lista mares
4. Muestra la longitud de la lista mares
5. Muestra los valores repetidos en la lista mares usando el método correspondiente
6. Elimina el tercer elemento de la lista mares y guárdalo en la variable mar1
7. Elimina el último elemento de la lista mares y guárdalo en la variable mar2
8. Guarda el valor del noveno elemento en la variable mar3
9. Muestra los valores de las variables mar1, mar2 y mar3
10.  Elimina el primer elemento de la lista mares con valor 'báltico'. Muestra la lista mares
11.  Elimina todos los elementos de la lista mares
12.  Ordena por orden alfabético de 'a' a 'z' los elementos de la lista mares1
13.  Ordena por orden alfabético de 'z' a 'a' los elementos de la lista mares2
'''

mares1 = ["mediterraneo", "cantábrico", "báltico", "adriático", "tirreno", "egeo"]

mares2 = ["rojo", "muerto", "caspio", "negro", "arábigo", "sulu"]

mares = [mares1[0], mares1[1], mares1[2], mares1[3], mares1[4], mares1[5],
         mares2[0], mares2[1], mares2[2], mares2[3], mares2[4], mares2[5]]

print("1. Cambia a la vez los valores de los elementos undécimo y duodécimo de la lista mares por los valores 'del norte' y 'alborán'. Muestra la lista mares")
mares[10] = "del norte"
mares[11] = "alboran"
print(mares)

print("2. En la lista mares, inserta un elemento más con el valor 'báltico'. Muestra la lista mares ")
mares.insert(12, "báltico")
print(mares)

print("3. Borra el quinto elemento de la lista mares. Muestra la lista mares ")
mares.pop(5)
print(mares)

print("4. Muestra la longitud de la lista mares ")
print(len(mares))

print("5. Muestra los valores repetidos en la lista mares usando el método correspondiente ")
x = []

for i in mares:
    if not i in mares:
        x.append(i)
print(i)


print("6. Elimina el tercer elemento de la lista mares y guárdalo en la variable mar1")
mar1 = mares[2]
mares.pop(2)
print(mares)
print(mar1)

print("7. Elimina el último elemento de la lista mares y guárdalo en la variable mar2")
mar2 = mares[-1]
mares.pop(-1)
print(mares)
print(mar2)

print("8. Guarda el valor del noveno elemento en la variable mar3")
mar3 = mares[8]

print("9. Muestra los valores de las variables mar1, mar2 y mar3")
print(f'Valor de mar1: {mar1} \nValor de mar2: {mar2} \nValor de mar3: {mar3}')

print("10.  Elimina el primer elemento de la lista mares con valor 'báltico'. Muestra la lista mares")
mares.remove("báltico")

print("11.  Elimina todos los elementos de la lista mares")
mares.clear()
print(mares)

print("12.  Ordena por orden alfabético de 'a' a 'z' los elementos de la lista mares1")
mares1.sort()
print(mares1)

print("13.  Ordena por orden alfabético de 'z' a 'a' los elementos de la lista mares2")
mares2.sort(key= None, reverse=True)
print(mares2)