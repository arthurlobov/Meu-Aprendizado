lista={}
lista['nome']=input('Nome do aluno: ')
lista['media']=float(input('Média do aluno:'))
print()
print(f'Nome é igual a: {lista["nome"]}')
print(f'Média é igual a {lista["media"]}')
if lista['media'] >= 7:
    print('Parabéns voce foi aprovado!')
elif lista['media'] < 5:
    print('Voce foi reprovado')
else:
    print('voce esta de recuperação.')
