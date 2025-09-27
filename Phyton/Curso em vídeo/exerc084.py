lista=list()
grupos=[]
nome=[]
pos=[]
cont=0
while True:
    lista.append(input('Nome: '))
    lista.append(int(input('Peso:')))
    a=input('deseja continuar [S] [N]?')
    grupos.append(lista[:])
    lista.clear()
    cont+=1
    if a in 'Nn':
        break
for item in grupos:
    maior=grupos[0][1]
    menor=grupos[0][1]
    nomem=grupos[0][0]
    nomep=grupos[0][0]
    if item[1] >= maior:
        maior=item[1]
        nomem=item[0]
        nome.append(nomem[:])

    elif item[1] <= menor:
        menor=item[1]
        nomep=item[0]
        pos.append(nomep[:])

print(f'o maior peso foi de {maior} Kg, peso de {nome}')
print(f'o menor peso foi de {menor} kg, peso de {pos}')
print(f'No total foram adicionas {cont} pessoas')