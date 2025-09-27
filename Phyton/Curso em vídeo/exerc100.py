from random import randint
from time import sleep

t = []
def sortear(*n):
    print('Sorteando os 5 valores: ',end='')
    for a in range(0,5):
        b=randint(0,9)
        t.append(b)
        print(f'{b:<2}',end='')
        sleep(0.5)
    print('FIM!')
def pares(p):
    print('O total de valores pares foram:',end='')
    s=0
    for e in p:
        if e % 2 == 0:
            print(f'{e:<2}',end='')
            s+=e
    print(f'\nA soma dos pares foi {s}')


sortear()
pares(t)