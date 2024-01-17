r1 = float(input('Digite um lado '))
r2 = float(input('Digite outro lado '))
r3 = float(input('Digite o último lado '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triangulo', end=' ')
    if r1 == r2 == r3:
        print('Eles formam um triangulo do tipo equilátero')
    elif r1 != r2 != r3 != r1:
        print('Esse triangulo é escaleno')
    else:
        print('isóciles')
else:
    print('Não pode formar um tríangulo')