
maior_peso = 0
menor_peso = 0

for i in range(1, 7):
    peso = float(input('Peso da {} pessoa '.format(i)))
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print('O maior peso lido foi {}' .format(maior_peso))
print('O menor peso lido é {}'.format(menor_peso))
