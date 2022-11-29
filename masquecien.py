'''
Escribe un programa en Python que pida al usuario dos números.

Si la suma de ambos números es mayor que 100 se mostrará el resultado de la suma y el
mensaje: 'La suma supera la centena'. De lo contrario se mostrará el resultado de la suma y el
mensaje ‘el resultado de la suma no supera la centena’.
'''

limit = 100

valOk = True

while valOk:

    try:
        num1 = int(input("Introduce un número "))
        num2 = int(input("Introduce otro número "))
        valOk = False
    except ValueError as error:
        print("Los numeros deben ser enteros")


res = num1 + num2


if res > limit:
    print("La suma supera la centena")
elif res == limit:
    print("La suma es igual a la centena")
else:
    print("El resultado de la suma no supera la centena")