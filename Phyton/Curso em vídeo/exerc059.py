c=int(input('digite um valor:'))
d=int(input('digite outro valor:'))
a=0
while a != 5:
    a=int(input('''Escolha um das opções:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] Novos números
    [5] sair so programa
    >>>>>>>>>>>>>Digite a opção escolhida: '''))
    print(' ')
    if a == 1:
        b = c+d
        print('A soma dos valores informados foi {}'.format(b))
    elif a == 2:
        b= c*d
        print('A multiplicação dos valores foi',b)
    elif a == 3:
        if c > d:
            print('O maior valor é {}'.format(c))
        else:
            print('O menor valor é {}'.format(d))
    elif a ==4:
        print('Informe os novo números')
        print(' ')
        c = int(input('digite um valor:'))
        d = int(input('digite outro valor:'))
    print('=-='*20)
    print(' ')
if a == 5:
    print('programa finalizado')