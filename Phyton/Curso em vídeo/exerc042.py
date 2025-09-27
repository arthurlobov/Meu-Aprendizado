a=float(input('Escreva o tamanho do lado 1:'))
b=float(input('Escreva o tamanho do lado 2:'))
c=float(input('Escreva o tamanho do lado 3:'))

if b+c >= a and a+c >= b and a+b >= c:
    print('Seu triângulo existe/')
    if a == b == c:
        print('Seu trângulo é equilatero')
    elif a == b or c == a or b == c:
        print('Seu trângulo é isosceles')
    else:
        print('Seu triângulo é escaleno')
else:
    print("Seu triângulo não existe")