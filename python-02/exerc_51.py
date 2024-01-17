num = int(input('Digite o número da PA: '))
razao = int(input('Digite a razão: '))
decimo = num + (10 - 1) * razao #esse é o calculo matematico

for c in range(num, decimo + razao, razao):
    fomula = num + razao
    print(c, end=' ')
print('Fim!')
