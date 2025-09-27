a=float(input('digite o tamanho do lado:'))
b=float(input('digite o tamanho do lado:'))
c=float(input('digite o tamanho do lado:'))

if c < a+b and b<c+a and a<c+b:
    print('Seu triângulo existe')
else:
    print('Seu triângulo não existe')
