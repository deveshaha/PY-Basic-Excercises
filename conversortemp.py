'''
Escribe un programa en Python que convierta la temperatura dada en grados Fahrenheit, si se
indica que son grados Celsius, o en grados Celsius, si se indica que son grados Fahrenheit.
'''

opc = int(input("Seleccione una opción \n1. Convertir de grados celcius a Farenheit \n2. Convertir de grados farenheint a Celcius "))


def celciusAfarenheint():
    valOk = True

    while valOk:

        try:
            c = float(input("Introduce los grados celcius "))
            valOk = False
        except ValueError as error:
            print("El valor introducido no es correcto, por favor intentalo de nuevo")

        f = (c * 1.8) + 32
        print(f'{c}ºC es igual a {f}ºF')


def farenheintAcelcius():
    valOk = True

    while valOk:

        try:
            f = float(input("Introduce los grados farenheint "))
            valOk = False
        except ValueError as error:
            print("El valor introducido no es correcto, por favor intentalo de nuevo")

        c = (f - 32) * 0.5556
        print(f'{f}ºF es igual a {c}ºC')

match opc:
    case 1:
        celciusAfarenheint()
    case 2:
        farenheintAcelcius()
    case _:
        print("El valor introducido no es correcto")

