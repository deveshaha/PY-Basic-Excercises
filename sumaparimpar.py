'''
Genera y muestra los números del 1 al 100 y calcula la suma de todos los números pares, por un
lado, y la suma de los números impares, por otro. Muestra los resultados.
'''

def generarArrays():
    global pares, impares, i
    pares = []
    impares = []
    for i in range(1, 101):
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)

def sumaPares():
    global sump, i
    sump = 0
    for i in pares:
        sump = sump + i

def sumaImpares():
    global sumimp, i
    sumimp = 0
    for i in impares:
        sumimp = sumimp + i

generarArrays()
sumaPares()
sumaImpares()

print(f'La suma de todos los numeros pares del 1 al 100 es: {sump}')
print(f'La suma de todos los numeros impares del 1 al 100 es: {sumimp}')
