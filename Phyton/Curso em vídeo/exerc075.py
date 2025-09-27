a=int(input('Digite um valor: '))
b=int(input('Digite um valor: '))
c=int(input('Digite um valor: '))
d=int(input('Digite um valor: '))
tupla=(a,b,c,d)
print(tupla)
print('Os número pares digitado foram:')
for p in tupla:
    if p % 2 == 0:
        print(p,end=' ')
if 9 in tupla:
    c9 = tupla.count(9)
    print('\nO nove paraeceu:',c9,'vezes')
if 3 in tupla:
    c3 = (tupla.index(3)) + 1
    print('O 3 apareceu na posição',c3)