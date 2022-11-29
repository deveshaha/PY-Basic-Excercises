'''
Escribe un programa en Python que calcule el área y el perímetro de un rectángulo pidiendo al
usuario que introduzca la base y la altura del mismo (con decimales).
'''

print("Calculo de área y perímetro de un rectangulo ")

base = float(input("Introduce la base del rectángulo "))
altura = float(input("Introduce la altura"))

print(f'El área del rectángulo es: {base * altura}')
print(f'El perimetro del rectangulo es: {(2*base) + (2*altura)}')