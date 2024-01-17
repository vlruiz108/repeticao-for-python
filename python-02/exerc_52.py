num = int(input('Digite um numero inteiro: '))
mult = 0

for c in range(1, num + 1):
    if num % c == 0:
        print(c)
        mult += 1
    else:
        print(c)
    print(f'{num} divisivel {mult} vezes')

if mult == 2:
    print(f'{num} é número primo')
else:
    print("Não é primo")
