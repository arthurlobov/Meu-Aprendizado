lista=[]
while True:
    lista.append(int(input('Digite um valor: ')))
    b=input('Deseja continuar [S/N]?')
    if b in 'Nn':
        break
print(f'os valores digitados foram: {lista}')
print(f'Os número pares digitado foram: ', end='')
for pos in lista:
    if pos % 2 ==0:
        print(f'{pos}...',end='')
print(f'\nOs números impares digitado foram: ',end='')
for pos in lista:
    if pos % 2 == 1:
        print(f'{pos}...',end='')