lista={}
cont=1
fem=[]
idade=[]
s=0
#perguntas
while True:
    lista['Nome']=input('Nome: ')
    lista['Sexo']=input('Sexo [M][F]: ').upper().strip()
    while lista['Sexo'] not in 'MF':
        lista['Sexo'] = input('Sexo [M][F]: ').upper().strip()
    lista['Idade'] = int(input('Idade: '))
    idade.append(lista['Idade'])
    c=input('Deseja continuar [S][N]? ').upper().strip()
    while c not in 'SN':
        c = input('Deseja continuar [S][N]? ').upper().strip()
#contas
    if lista ['Sexo'] == 'F':
        fem.append(lista['Nome'])
    s += lista['Idade']
    if c == 'N':
        break
    cont += 1
media=s/len(idade)
#resposta
print(f'Ao todo são {cont} pessoas cadastradas')
print(f'As mulheres cadastradas foram: {fem}')
print(f'A média de idades foi {media}')
f=[]
f=lista.values()
for e,v in enumerate(f):
    print(f'O {e[0]}')