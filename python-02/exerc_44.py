preco = float(input('Digite o valor do produto '))
print('''
[1] a vista ou cheque
[2] a vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão
''')
opcao = int(input('Qual a opção '))
if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra vai custar {:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    totalparcela = int(input('Quantas parcelas '))
    parcela = total / totalparcela
    print('Sua compra vai custar {:.2f}'.format(parcela))
print('Sua compra custou {:.2f} e o valor será {:.2f}'.format(preco, total))
