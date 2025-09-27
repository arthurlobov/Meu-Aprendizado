galera=[]
pessoa={}
fem=[]
soma=0
#perguntas
while True:
    pessoa.clear()
    pessoa['nome']=input('Nome: ')
    pessoa['sexo']=input('Sexo [M][F]: ').upper().strip()
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = input('Sexo [M][F]: ').upper().strip()
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    c=input('Deseja continuar [S][N]? ').upper().strip()
    while c not in 'SN':
        c = input('Deseja continuar [S][N]? ').upper().strip()
    soma += pessoa['idade']
    if pessoa['sexo'] == 'F':
        fem.append(pessoa['nome'])
    if c == 'N':
        break
media=soma/len(galera)
#resposta
print(galera)
print(f'A quantidade de pessoas inscritas na lista foram {len(galera)}')
print(f'A media de idade das pessoas cadastradas foi: {media}')
print(f'A quantidade de mulheres foi {len(fem)} e as mulheres foram {fem}')
print('Lista de pessoas que estão acima da média:')
if pessoa['idade'] >= media:
    print(f'Nome = {pessoa["nome"]}; Idade = {pessoa["idade"]}; Sexo = {pessoa["sexo"]}')
