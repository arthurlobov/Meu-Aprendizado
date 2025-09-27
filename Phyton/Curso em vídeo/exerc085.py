lista=[[],[]]
for n in range(0,7):
    a=(int(input(f'digite o {n+1}° valor: ')))
    if  a % 2 == 0:
        lista[0].append(a)
    if a % 2 == 1:
       lista[1].append(a)
print(f'os valore impares digitados foram {sorted(lista[0])}')
print(f'os valore pares digitados foram {sorted(lista[1])}')