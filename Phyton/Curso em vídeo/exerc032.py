from datetime import date
a=int(input('digite o ano:'))
b= a % 4
d = int(date.today().year)
e= d % 4
if e == 0:
    print('Esse ano é Bissexto', d)
if b == 0 and a % 100 !=0 or a % 400 == 0:
    print('Esse ano é Bissexto')
else:
    print('Esse ano não é bissexto')
