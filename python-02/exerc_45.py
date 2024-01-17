from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')

print('''
[0] Pedra
[1] Papel
[2] Tesoura
''')

escolha = int(input('Escolha uma opção de 0 a 2: '))

if escolha < 0 or escolha > 2:
    print('Jogada inválida. Escolha um número de 0 a 2.')
else:
    computador = randint(0, 2)
    print('Computador jogou: {}'.format(itens[computador]))
    print('Você escolheu: {}'.format(itens[escolha]))

    if escolha == computador:
        print('Empate')
    elif (escolha == 0 and computador == 2) or (escolha == 1 and computador == 0) or (escolha == 2 and computador == 1):
        print('Jogador vence')
    else:
        print('Computador vence')
