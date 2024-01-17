peso = float(input('Digite seu peso '))
altuta = float(input(('Digite sua altura ')))
imc = peso/(altuta ** 2)

if imc < 18.5:
    print('O seu ima é de {:.2f} está abixo do peso'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('O seu imc é de {:.2f} está com peso ideal'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu imac é de {:.2f} vc está com sobrepeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu imc é de {:.2f} vc está com obesidade' . format(imc))
else:
    imc > 40
    print('Você está com imc {:.2f} está com obesidade morbida'.format(imc))
