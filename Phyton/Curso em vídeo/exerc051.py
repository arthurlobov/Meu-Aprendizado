print('='*30)
print('    10 termos de uma P.A.')
print('='*30)
c=int(input('Digite um número: '))
d=int(input('digite a razão do número: '))
for a in range (0,11):
    print('{} -> '.format(c+a*d), end=' ')
print('Acabou')

