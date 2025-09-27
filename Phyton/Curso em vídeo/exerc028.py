from random import randint
print('-=-'*20)
s=int(input('Vou pensar em um númera entre 0 e 10, advinhe.'))
c=randint(1, 10)
print('-=-'*20)
if c == s:
    print('Parabéns você acertou')
else:
    print('Errou')
print(c)
