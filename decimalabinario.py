# Convertir de número decimal a binario

decimal = int(input("número decimal: "))
numero = decimal

binario = 0
i = 0
while (decimal > 0):

    digito = decimal % 2
    decimal = int(decimal // 2)
    binario = binario + digito * (10**i)
    i = i+1

print(f'{numero} en binario -> {binario}')