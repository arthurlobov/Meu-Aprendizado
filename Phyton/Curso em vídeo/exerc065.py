cont=1
num = float(input('Escolha um número: '))
escolha = str(input('Você deseja continuar [s/n]:')).upper().strip()[0]
total=menor=maior=num
media= num/cont
if escolha == 'S':
    while escolha != 'N':
        num = float(input('Escolha um número: '))
        escolha = str(input('Você deseja continuar [s/n]:')).upper().strip()[0]
        total += num
        #contador
        cont+=1
        #maior
        if num > maior:
            maior = num
        #Menor
        elif num < menor:
            menor= num
        #média aritimétrica
media= total/cont
print('Você digitou {} números, sendo o maior {} e o menor {}. A média dos valores digitados foi {}'.format(cont,maior,menor,media))