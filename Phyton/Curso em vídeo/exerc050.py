soma=0
cont=0
for a in range (1,7):
    b=int(input('Digite um valor: '))
    if b % 2 == 0:
        soma += b
        cont += +1
print('A soma dos {} deu: {}'.format(cont,soma))