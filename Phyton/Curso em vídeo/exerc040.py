a=float(input('Primeira nota: '))
b=float(input('Segunda nota: '))
x=(a+b)/2
if x < 5:
    print('Reprovado com {} por {} pontos de diferença'.format(x,-(7-x)))
elif x >= 7:
    print('Aprovado com {} por {} pontos de diferença'.format(x,-(7-x)))
elif 5 <= x <= 6.9:
    print('Está em recuperação com {} por {} pontos de diferença'.format(x,-(7-x)))