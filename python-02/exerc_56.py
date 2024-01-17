soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
mulheres_20 = 0


for p in range(1, 5):
    nome = str(input('Nome: ')).split()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] ')).upper()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and mulheres_20 < 20:
        mulheres_20 += 1

media_idade = soma_idade/4
print(f'A media da idade das pessoas é {media_idade}')
print(f'O nome do homem mais velho {maior_idade_homem} e se chama {nome_velho}')
print(f'O total de mulheres com menos de 20 anos {mulheres_20}')
