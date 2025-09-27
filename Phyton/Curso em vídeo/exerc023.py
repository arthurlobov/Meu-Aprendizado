a=int(input('Escreva um número'))
u=a//1%10
d=a//10%10
c=a//100%10
m=a//1000%10
print('Seu numero possuí {} unidades'.format(u))
print('Seu número possuí {} dezenas'.format(d))
print('Seu número possuí {} centenas'.format(c))
print('Seu número possuí {} milhares'.format(m))