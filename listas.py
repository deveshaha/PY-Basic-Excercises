'''
• Archivo que debes crear ➔ listas.py

• Escribe un programa en Python que cree una lista NO protegida llamada mares1 con 6
posiciones (mediterráneo, cantábrico, báltico, adriático, tirreno, egeo).
• Crea otra lista llamada mares2 con 6 posiciones (rojo, muerto, caspio, negro, arábigo, sulu).
• Se creará también una lista nueva llamada mares que tenga 12 posiciones que serán las 6
• posiciones de mares1 más las 6 posiciones de mares2.
• El programa mostrará la siguiente información:

1. La longitud de la lista mares1
2. Los valores de todas las posiciones de la lista mares1
3. La longitud de la lista mares2
4. Los valores de todas las posiciones de la lista mares2
5. La longitud de la lista mares
6. Los valores de todas las posiciones de mares
7. Los valores de las posiciones 1, 2 y 3 de mares1
8. El índice o posición del mar egeo en mares1
9. Los valores de las posiciones 4, 5 y 6 de mares2
10.  El índice o posición del mar caspio en mares2
11.  El índice o posición del mar caspio en mares

'''

mares1 = ["mediterraneo", "cantábrico", "báltico", "adriático", "tirreno", "egeo"]

mares2 = ["rojo", "muerto", "caspio", "negro", "arábigo", "sulu"]

mares = []

for i in mares1:
    mares.append(i)

for i in mares2:
    mares.append(i)

print(mares)

# mares = [mares1[0], mares1[1], mares1[2], mares1[3], mares1[4], mares1[5],
#          mares2[0], mares2[1], mares2[2], mares2[3], mares2[4], mares2[5]]

print(f'La lngitud del mares1 es {len(mares1)}')
print(f'Los valores de todas las posiciones de la lista mares1: {mares1}')
print(f'La lngitud del mares2 es {len(mares2)}')
print(f'Los valores de todas las posiciones de la lista mares2: {mares2}')
print(f'Los valores de todas las posiciones de la lista mares: {mares}')
print(f'Los valores de las posiciones 1, 2 y 3 de mares1: {mares1[0], mares1[1], mares1[2]}')
print(f'El índice o posición del mar egeo en mares1: {mares1.index("egeo")}')
print(f'Los valores de las posiciones 4, 5 y 6 de mares2: {mares2[3], mares2[4], mares2[5]}')
print(f'El índice o posición del mar caspio en mares2: {mares2.index("caspio")}')
print(f'El índice o posición del mar caspio en mares: {mares.index("caspio")}')

