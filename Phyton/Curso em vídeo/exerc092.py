from operator import itemgetter

dicionario={}
dicionario['nome']=input('Nome: ')
dicionario['nascimento']=input('Ano de nascimento: ')
dicionario['N carteira de trabalho']=int(input('Carteira de trabalho (0 não tem): '))
if dicionario['N carteira de trabalho'] != 0:
    dicionario['ano de contratação']=int(input('Ano de contratação: '))
    dicionario['salario']=float(input('salário: '))
lista=[]
lista= dicionario.items()
print('-=-'*20)
for i,v in enumerate(lista):
    print(f'{v[0]} tem o valor igual: {v[1]}')
