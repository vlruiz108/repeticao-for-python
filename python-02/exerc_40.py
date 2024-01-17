nota1 = float(input("Digite uma nota "))
nota2 = float(input("Digite outra nota "))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Sua sua nota média foi {media} por tanto está reprovado!')
elif media >= 5 and media <= 6.9:
    print(f'Sua media foi {media} você está de recuperação!')
else:
    media > 7 and media == 10
    print(f'Sua media foi {media} parabéns, está aprovado!')
