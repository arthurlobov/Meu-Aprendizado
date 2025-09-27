lista=[]
while True:
    a=int(input('Digite um valor: '))
    if a not in lista:
        lista.append(a)
    else:
        print('Esse número já está na lista')
    b = input('deseja continuar [S/N]?').strip().upper()
    if b not in 'SN':
        print('resposta invalida...')
        b = input('deseja continuar [S/N]?').strip().upper()
    if b == 'N':
        break
print(sorted(lista))