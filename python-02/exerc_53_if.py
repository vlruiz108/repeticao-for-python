frase = str(input('Digite uma frase: ')).replace(' ', '').lower()
fraseSemEspaco = frase[::-1]

if frase == fraseSemEspaco:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')
