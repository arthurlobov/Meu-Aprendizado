a=input('Digite uma frase: ').strip().upper()
c=a.split()
d=''.join(c)
inverso =''
for e in range (len(d)-1,-1,-1):
    inverso += d[e]
if inverso == d:
    print('A palavra {} é um palíndromo'.format(inverso),end=' ')
else:
    print(' A palavra {} não é um palindromo'.format(d),end=' ')

