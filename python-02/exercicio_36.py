casa = float(input('Digite o valor da casa: '))
salario = float(input('Salario R$: '))
anos = int(input('Quantidade de anos que vai pagar: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('O valor da casa R${:.2f} pago em tantos anos' .format(casa, anos), end=' ')
print('a prestaçao {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo liberado')
else:
    print('Emprestimo negado')
