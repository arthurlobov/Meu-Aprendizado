total=0
a = 0
cont=0
a=int(input('Digite um número [Use 999 para parar]: '))
while a != 999:
    total+=a
    cont+=1
    a = int(input('Digite um número [Use 999 para parar]: '))
print('Você digitou {} números e asoma foi: {} '.format(cont,total))