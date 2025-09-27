from random import randint
ficha=[]
n='JOGA NA MEGA CENA'
print('-=-'*30)
print(f'{n:^85}')
print('-=-'*30)

a=int(input('Quantos jogos voce vai querer que eu sorteie?'))
for b in range (0,a):
    print(f'Jogo {b+1}: ',end='')
    for c in range(0,6):
        a=randint(0, 60)
        ficha.append(a)
    ficha.sort()
    print(ficha)
    ficha.clear()
