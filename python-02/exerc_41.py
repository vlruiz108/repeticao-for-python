from datetime import date

ano_atual = date.today()

nome_atleta = str(input('Digite o nome do atleta: '))
ano_nascimento = int(input('Que ano o atleta nasceu: '))
idade = ano_atual.year - ano_nascimento
if idade <= 9:
    print(f'O {nome_atleta} tem {idade} anos é atleta mirim')
elif idade > 9 and idade <= 14:
    print(f'O {nome_atleta} tem {idade} anos é um atleta infantil')
elif idade > 14 and idade <= 19:
    print(f'O {nome_atleta} tem {idade} anos é um atleta júnior')
elif idade > 19 and idade <= 25:
    print(f'O {nome_atleta} tem {idade} anos é um atleta sênior')
else:
    print(f'O {nome_atleta} tem {idade} anos é um atleta master')
