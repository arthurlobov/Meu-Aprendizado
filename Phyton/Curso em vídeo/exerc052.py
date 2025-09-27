tot=0
a=int(input('Escreva o número:'))
for b in range (1,a+1,1):
    if a % b == 0:
        print('\033[31m',end=' ')
        print(b,end=' ')
        tot += 1
    else:
        print('\033[m',end=' ')
        print(b, end=' ')
if tot == 2:
    print('\033[m')
    print('O número {} foi divido {} vezes, logo ele é primo'.format(a,2))
else:
    print('\033[m')
    print('O número {} foi divido {} vezes, logo ele não é primo'.format(a,tot))





