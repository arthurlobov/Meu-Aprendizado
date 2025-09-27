cont=0
lista=[]
while True:
    cont+=1
    lista.append(int(input('Digite um número:')))
    b=input('deseja continuar [S/N]: ').upper().strip()
    if b == 'N':
        break
lista.sort(reverse=True)
print(f'Seus valores em ordem decrescente foram {lista}')
print(f'Você digitou {cont} valores')
if 5 in lista:
    print('o valor 5 esta na lista!')
if 5 not in lista:
    print('O valor 5 não esta na lista')