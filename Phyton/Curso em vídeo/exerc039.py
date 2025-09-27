from datetime import date
z= date.today().year
a=int(input('Ano de nascimento: '))
b= z - a
c=b-18
if b >= 19:
    print('Seu alistamento está atrasado em {} anos, se aliste urgentemente, tal devia ter sido feito em {}'.format(c,2025-c))
elif b <= 17:
    print("Seu alistamento está em dias, faltam {} anos para seu alistamento obrigatório em {}".format(-c, 2025-c))
elif b == 18:
    print('Seu alistamento deve ser feito esse ano, se aliste urgentemente')