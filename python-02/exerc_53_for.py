frase = str(input('Digite uma frase ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto),):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo')
