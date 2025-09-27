#primeira parte
def contagem (i,f,r):
    print('--'*20)
    c=i-1
    while c < f:
        c+=r
        print(f'{c:<2}',end='')
    print(' FIM!!')
    print()
#parte modulavel
def negativo(a,b,c):
    print('-'*20)
    while a >= b:
        print(f' {a}',end='')
        a -= c
    print()


#P.P
contagem(1,10,1)
negativo(10,0,2)

#personalizada
print('-'*20)
print('Chegou a sua vez de personalizar')
print()
i=int(input('início:'))
f=int(input('Fim:'))
r=int(input('Razão:'))
negativo(i,f,r)