num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 > num2:
    print('O {} primeiro numero é maior que o {}' .format(num1, num2))
elif num2 > num1:
    print('O maior numero é o segundo {} e o 2º maior número é {}'.format(num2, num1))
else:
    print('Os numeros são iguais' .format(num1, num2))
