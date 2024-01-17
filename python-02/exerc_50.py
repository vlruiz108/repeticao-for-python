soma = 0
cont = 0

for num in range(1, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você contou {cont} numeros pares que somados dão {soma}')
