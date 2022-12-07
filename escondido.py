'''
• Escribe un programa en Python que permita calcular el número que esconde. El usuario debe
averiguar qué número esconde el programa. Se pide números al usuario y se le informará de si
el número es más grande o es más pequeño que el número a averiguar. Si lo acierta, se le
informará con el mensaje correspondiente.

• Muestra cuántas veces ha introducido un número erróneo el usuario hasta dar con el número
correcto. Una vez descubierto, si lo ha acertado en el primer intento, se mostrará el mensaje
“¡Enhorabuena! Lo has acertado a la primera”, si el número de veces es mayor que 3, se mostrará el
mensaje: “Por fin lo has acertado. Ha debido ser muy complicado para ti”. En otros casos, se mostrará el
mensaje: “Buen Trabajo! Lo has acertado”.
'''

import random

num = random.randint(1, 100)
numUser = 0
intentos = 0

print(num)

while numUser != num:
    try:
        numUser = int(input("Introduce un número "))
        intentos += 1
    except ValueError as error:
        print("El valor introducido no es correcto")

    if numUser > num:
        print("El número es más pequeño")
    elif numUser < num:
        print("El número es más grande")

if intentos == 1:
    print("¡Enhorabuena! Lo has acertado a la primera")
elif intentos > 3:
    print("Por fin lo has acertado. Ha debido ser muy complicado para ti")
else:
    print("Buen Trabajo! Lo has acertado")

print(f'Has necesitado {intentos} intentos para acertar')

