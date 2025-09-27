a=float(input('Digite seu peso em (KG): '))
b=float(input('Digite sua altura em metros (m): '))
c=a/b**2
print("Seu calculo IMC deu: {:.2fq}".format(c))

if c <= 18.5:
    print('Você está abaixo do peso')
elif c > 18.5 and c <= 25:
    print('Você está no peso ideal')
elif c > 25 and c <= 30:
    print('Você está sobrepeso')
elif c > 30 and c <= 40:
    print('Você está obeso')
else:
    print('Você possuí obsidade morbida')