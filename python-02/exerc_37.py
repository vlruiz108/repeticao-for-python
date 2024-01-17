num = int(input('Numero qualquer '))
print('''Escolha uma opção:
      [1] para Binario
      [2] para octal
      [3] para hexadecimal''')
opcao = int(input('Digite uma opção: '))
if opcao == 1:
    print('O {} que vc escolheu é {} em binario' .format(num, bin(num)[2:]))
elif opcao == 2:
    print('O numero que vc escolha {} e {} em octal'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O numero {} que vc escolheu é {} em hexadecimal' .format(num, hex(num) [2:]))