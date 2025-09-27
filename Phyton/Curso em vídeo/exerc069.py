ti=tsm=tsf=0
while True:
    print('-'*30)
    print('Cadatre uma pessoa')
    print('-'*30)
    i=int(input('idade:'))
    s=input('Sexo [M] [F]').strip().upper()
#sexo invalido
    while s not in 'MmFf':
        print('''Informação invalida
        Por favor tente novamente...''')
        s = input('Sexo [M] [F]').strip().upper()[0]
#contadores
    if i >= 18:
        ti+=1
    if s == 'M':
        tsm+=1
    if s == 'F' and i >= 20:
        tsf+=1
#Deseja continuar
    print('-'*30)
    c=input('Quer continuar [S] [N]: ').strip().upper()[0]
    print('-'*30)
#quer continuar invalido
    while c not in 'SN':
        print('''Informação invalida
        Por favor tente novamente...''')
        c = input('Quer continuar [S] [N]: ').strip().upper()[0]
    if c == 'N':
        break
#Resultado
print(f'''No total são {tsm} homens  
{tsf} mulheres acima de 20 anos
São {ti} pessoas acima dos 18 anos''' )

