matriz=[[0,0,0],[0,0,0],[0,0,0]]
soma=somac=somal=0
for l in range(0,3):
    for c in range(0,3):
        a=matriz[l][c]=int(input(f'digite o valor [{l}][{c}]: '))
        if a % 2 == 0:
            soma+=matriz[l][c]
    somac += matriz[l][2]
    somal += matriz[2][l]
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()

print(f'A soma da coluna 3 da matriz é {somac}')
print(f'A soma da linha 3 da matriz é {somal}')
print(f'a soma dos pares da matriz é {soma}')