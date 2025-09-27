print('='*30)
print('----------LOJAS LOBO----------')
print('='*30)
cont=soma=sv=menor=0
while True:
    #váriaveis principais
    print('-' * 30)
    p=input('Nome do produto: ')
    v=float(input('Preço: RS '))
    print('-' * 30)
    #Cálculos
    soma+=v
    cont+=1
    if cont == 1:
        menor=v
    if v < menor:
        menor=v
    if v > 1000:
        sv+=1
    #continuar
    c=input('Quer continuar? [S] [N]').strip().upper()
    if c not in 'SN':
        print('''Informações iválidas
        tente novamente...''')
        c = input('Quer continuar? [S] [N]').strip().upper()
    elif c == 'N':
        break
print(f'''
O total da compra foi {soma:.2f}
Temos {sv::.2f} produtos custando mais de 1000RS
O produto mais barato foi {menor:.2f}''')