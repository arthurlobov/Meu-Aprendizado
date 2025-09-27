listanum=[]
for a in range (0,5):
    listanum.append(int(input(f'digite um valor para a posição {a}: ')))
    if a == 0:
        maior = menor = listanum[a]
    if listanum[a] > maior:
        maior=listanum[a]
    if listanum[a] < menor:
        menor=listanum[a]
print(f'\nVocê digitou os valores {listanum}')
print(f'O maior valor foi {maior} e esta nas posições: ',end='')
for i,v in enumerate(listanum):
    if v == maior:
        print(f'{i}...',end=' ')
print()
print(f'O menor valor foi {menor} e esta nas posições: ',end='')
for x,y in enumerate(listanum):
    if y == menor:
        print(f'{x}...',end='')
print()