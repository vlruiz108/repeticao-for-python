from datetime import date

ano_atual = date.today()

ano_nascimento = int(input('Digite o ano do seu nascimento: '))

idade = ano_atual.year - ano_nascimento
if idade <= 17:
    print('Você tem {} anos e ainda não pode se alistar falta {} anos' .format(idade, 18 - idade))
elif idade == 18:
    print('Vc tem {} precisa se alistar'.format(idade))
elif idade > 21:
    print('Vc tem {} anos e já passou {} anos do tempo de alistamento' .format(idade, idade - 18))
