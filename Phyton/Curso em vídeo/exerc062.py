
primeiro=int(input('primeiro termo: '))
razao=int(input('Razão: '))
cont=0
total=0
adicional=10
while adicional != 0:
    total=total+adicional;
    while cont <= total:
        cont +=1
        soma = primeiro + razao * cont
        print(soma,'->',end=' ')
    print('Pausa')
    adicional=int(input('Quantos elementos você deseja adicionar? '))
print('Sua P.A. tem um total de {} termos'.format(total))