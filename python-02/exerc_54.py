from datetime import date

ano_atual = date.today()

maior_idade = menor_idade = 0

for pessoa in range(1, 8):
    ano_nasc = int(input('Digite seu ano de nascimento: '))
    idade = ano_atual.year - ano_nasc
    if idade >= 21:
        maior_idade += 1
    else:
        idade < 21
        menor_idade += 1

print(f'{menor_idade} são menor de idade e {maior_idade} são maior de idade')
