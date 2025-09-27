
produtos=('lapis',1,'caneta',2,'caderno',12,
          'mesa',212.5)
lojaslobo = 'LOJAS LOBO'
print(f'{lojaslobo:^40}')
print('-=-'*14)
for pos in range(0, len(produtos)):
    if pos % 2 ==0:
        print(f'{produtos[pos]:.<30}',end=' ')
    if pos % 2 ==1:
        print(f'{produtos[pos]:>0.2f} RS')
print('-=-' * 14)