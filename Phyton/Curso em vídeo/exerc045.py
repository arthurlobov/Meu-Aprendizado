from random import randint
from time import sleep

print('''
[1] Tesoura
[2] Pedra
[3] Papel''')

x=int(input('Qual a sua jogada?'))

a=('pedra','papel','tesoura')
b=randint(1,3)

print('jo')
sleep(1)
print('ken')
sleep(1)
print('po')
sleep(1)

print('-=-'*10)
if b == 1:
    if x == 1:
        print('O Jogador escolheu tesoura')
        print('A máquina escolheu tesoura')
        print('Empate!')
    elif x == 2:
        print('O jogador escolheu pedra')
        print('A máquina escolheu tesoura')
        print('Jogador Vence!')
    elif x == 3:
        print('O jogador escolheu papel')
        print('A máquina escolheu tesoura')
        print('A máquina Venceu!')
elif b == 2:
    if x == 1:
        print('O Jogador escolheu tesoura')
        print('A máquina escolheu pedra')
        print('A maquina venceu!')
    elif x == 2:
        print('O jogador escolheu pedra')
        print('A máquina escolheu pedra')
        print('Empate!')
    elif x == 3:
        print('O jogador escolheu papel')
        print('A máquina escolheu pedra')
        print('O jogador venceu!')
elif b == 3:
    if x == 1:
        print('O Jogador escolheu tesoura')
        print('A máquina escolheu papel')
        print('o jogador Venceu!')
    elif x == 2:
        print('O jogador escolheu pedra')
        print('A máquina escolheu papel')
        print('A máquina venceu!')
    elif x == 3:
        print('O jogador escolheu papel')
        print('A máquina escolheu papel')
        print('Empate!')
print('-=-'*10)