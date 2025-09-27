print('-'*30)
print('seguência de fibonacci')
print('-'*30)
elementos=1
while elementos != 0:
    elementos = int(input('Quantos deseja adicionar: '))
    t1=0
    t2=1
    t3=t1+t2
    cont=3
    print(t1,t2,end=' ')
    while cont <= elementos:
        cont+=1
        t3=t1+t2
        print(t3,end=' ')
        t1=t2
        t2=t3
    print('-> FIM')
