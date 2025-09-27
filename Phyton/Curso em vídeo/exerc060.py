from math import factorial
a=int(input('Escreva o fatorial: '))
b=factorial(a)
c=a+1
print('calculando {} fatorial:'.format(a),end=' ')
while c != 1:
    c -= 1
    if c == 1:
        print('{} = {}'.format(c,b))
    else:
        print('{} x'.format(c),end=' ')


