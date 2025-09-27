cadastroj={}
lista=[]
s=0
cadastroj['nome']=input('Nome do jogador: ')
cadastroj['partidas']= int(input(f'Quantas partidas {cadastroj["nome"]} jogou? '))
for b in range (0,cadastroj['partidas']):
    lista.append(int(input(f'Quantos gols {cadastroj["nome"]} fez? ')))
    cadastroj['gol']=lista
for e in lista:
    s+=e
cadastroj['total']=s

print('-=-'*20)
print(cadastroj)
print('-=-'*20)
c=[]
c=cadastroj.items()
for e,v in enumerate(c):
    print(f'o campo {v[0]} tem valor {v[1]}')
print('-=-'*20)
print(f'''O jodagor {cadastroj["nome"]} jogou {cadastroj["partidas"]} partidas''')
for e,i in enumerate(lista):
    print(f'Na partida {e} o jogador fez {i} gols')
print(f'Foi um total de {cadastroj["total"]} gols')