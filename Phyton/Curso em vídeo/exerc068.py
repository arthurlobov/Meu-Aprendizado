from random import randint
cont=0
while True:
    variavel=int(input('Digite o seu número: '))
    compt = randint(0, 9)
    pi=input('Escolha par ou ímpar [P] ou [I]: ').strip().upper()
    s = variavel + compt
    r = s % 2
    while pi not in 'PI':
        print('Variavel ilegivel')
        pi = input('Escolha par ou ímpar [P] ou [I]: ').strip().upper()
    if pi == 'P':
        if r == 0:
            print('-' * 50)
            print('Parabéns você venceu')
            print('-' * 50)
        elif r == 1:
            print('-'*50)
            print('voce perdeu')
            break
    elif pi == 'I':
        if r == 0:
            print('-' * 50)
            print('voce perdeu')
            break
        elif r == 1:
            print('-' * 50)
            print('voce venceu')
            print('-' * 50)
    cont+=1
print('-'*50)
print(f'''Parabéns!!! Você venceu {cont} vezes. Obrigado por jogar!''')

