an=[]
nota=[]
media=[]
cont=0
while True:
    an.append(input('Nome: '))
    an.append(float((input('Nota 1: '))))
    an.append(float((input('Nota 2: '))))
    nota.append(an[:])
    an.clear()
    resp=input('Deseja continuar? ')
    if resp in 'Nn':
        break
    while resp not in 'Ss':
        resp = input('Deseja continuar? ')
for e in nota:
    media.append((e[1]+e[2])/2)
print('-=-'*20)
nome='NOME'
print(f'N {nome:<10}MÉDIA')
print('---'*20)
for a in range(len(nota)):
    print(f'{a:} {nota[a][0]:<10}{media[a]:^.1f}')
    cont += 1
while True:
    a=int(input('Mostra notas de qual aluno? '))
    if a == 999:
        print('-'*30)
        print('Volte Sempre')
        break
    while a > len(nota):
        a = int(input('Mostra notas de qual aluno [interromper: 999]? '))
    else:
        print(f'As notas de {nota[a][0]} são: [{nota[a][1]} , {nota[a][2]}]')
