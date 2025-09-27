a=0
while True:
    a=int(input('Quer a tabuada de que valor? '))
    if a < 0:
        break
    print('-'*30)
    for b in range (1,11):
        c=a*b
        print(f'{a} x {b} = {c}')
    print('-'*30)
print('-'*30)
print('Obrigado pela preferência, volte sempre')