a=float(input('Sua viagem possuí quantos kilometros?'))
if a <= 200:
    b=a*0.5
    print('Sua viagem custa {} RS'.format(b))
if a >= 201:
    c = a * 0.45
    print('Sua viagem custa {}'.format(c))
