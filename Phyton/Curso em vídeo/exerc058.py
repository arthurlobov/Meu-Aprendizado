from random import randint
c=randint(0,10)
cont=0
a=int(input('Informe um número: '))
while a != c:
    cont += 1
    if a < c:
        a=int(input('O seu número é menor que o pensado pelo computador, tente novamente: '))
    elif a > c:
        a=int(input('O seu número é maior que o pensado pelo computador, tente novamente: '))
print('Parábens você acertou! O número pensado foi {}, você tentou {} vezes'.format(a,cont))