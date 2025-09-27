tupla=('Arthur','Lobo','Vieira','Elylly','Lara','rhyan','heitor','julia')
for pos in tupla:
    print(f'\nA palavra {pos} tem as vogais:',end=' ')
    for letra in pos:
        if letra in 'Aa':
            print(letra,end=' ')
        if letra in 'Ee':
            print(letra,end=' ')
        if letra in 'Ii':
            print(letra,end=' ')
        if letra in 'Oo':
            print(letra,end=' ')
        if letra in 'Uu':
            print(letra,end=' ')