from operator import itemgetter
from random import randint
from time import sleep
p={ 'Jogador1': randint (1,6), 'Jogador2':randint(1,6),
    'jogador3':randint(1,6),'jogador4':randint(1,6)
}
for k,v in p.items():
    print((f'O {k} tirou {v}'))
print('-=-'*10)
print(f'{"RAKING DOS JOGADORES":^20}')
r=[]
r=sorted(p.items(),key=itemgetter(1),reverse=True)
print(r)
for i,v in enumerate(r):
    print(f'o {i+1}° é do {v[0]} com {v[1]}')