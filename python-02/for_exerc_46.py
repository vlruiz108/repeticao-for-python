from time import sleep
print('Inicio da contagem')

sleep(0.3)

for c in range(10, -1, -1):
    print(c)
    sleep(0.1)

print('Contagem finalizada!')
