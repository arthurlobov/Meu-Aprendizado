from random import randint
t=0
print('Os valoras sorteado foram: ',end=' ')
a=(randint(1,9),randint(1,9),randint(1,9),randint(1,9),randint(1,9),)
print('Os valoras sorteado foram: {} '.format(a))
print(f'O maior valor sorteado foi {max(a)}',end=' ')
print(f'\n O menor valor sorteado foi {min(a)}')