tabuada = int(input('Digite uma tabuada: '))
num_inicial = 0
num_final = 10

for num in range(num_inicial, num_final + 1):
    resultado = tabuada * num
    print(f'O numero da tabuada selecionado foi {tabuada} x {num} vai ser igual a {resultado}')
