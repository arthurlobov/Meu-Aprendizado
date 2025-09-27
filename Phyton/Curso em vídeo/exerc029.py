r=int(input('Qual a velocidade do carro?'))

if r <=80:
    print('ae')
if r >=81:
    v=(r-80)*7
    print('a sua multa foi de', v,'RS')