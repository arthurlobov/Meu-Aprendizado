times=('atletico','minas','fortaleza','real madri','barça','paris sngerman',
       'nova iguaçu','são paulo','atletico madrid','ribeirão preto')
c5=times[0:5]
c4=times[-5:-1]
o=sorted(times)
c=(times.index('fortaleza'))+1
print(' ')
print('BRASILEIRÃO'.center(160))
print(' ')
print('-=-'*60)
print(f'Lista de times do brasileirão: {times}')
print('-=-'*60)
print(f'Os cincos primeiros são: {c5}')
print('-=-'*60)
print(f'Os quatro últimos são: {c4}')
print('-=-'*60)
print(f'Os times em ordem alfabética são: {o}')
print('-=-'*60)
print(f'O fortaleza esta na {c} posição')