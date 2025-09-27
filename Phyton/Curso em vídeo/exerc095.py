jogador={}
tot=[]
gol=[]
while True:
    gol.clear()
    jogador.clear()
    jogador['nome']=input('Nome do jogador: ')
    jogador['jogo']=int(input(f'Quantos jogos o {jogador["nome"]} jogou: '))
    for a in range(0,jogador['jogo']):
        g=int(input(f'Quantidade de gols na partida {a}:'))
        gol.append(g)
        jogador['gols'] = gol.copy()
    jogador['total']=sum(gol)
    tot.append(jogador.copy())
    resp=input('Desaja continuar [S][N]?').upper()[0]
    while resp not in 'SN':
        print('Tente novamente...')
        resp = input('Desaja continuar [S][N]?').upper()[0]
    if resp == 'N':
        break

print('-=-'*20)
print('n.',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
for k,i in enumerate(tot):
    print(f' {k}',end='')
    for e in i.values():
        print(f'{str(e):<15}',end='')
    print()
print()
while True:
    j=int(input('você quer mostrar os dados de qual jogador?[Digite 999 para parar]'))
    while j > len(tot):
        print('tente novamente...')
        j = int(input('você quer mostrar os dados de qual jogador?[Digite 999 para parar]'))
    print(f'O jogador escolhido foi {tot[j]["nome"]}')
    for k,v in enumerate(tot[j]["gols"]):
        print(f'Na partida {k} o jogador fez {v} gols')
    if j == 999:
        break
