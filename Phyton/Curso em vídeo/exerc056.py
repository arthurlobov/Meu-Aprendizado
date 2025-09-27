media=0
contador=0
maior=0
menor=0
mnome=0
mnnome=0
tot=0
meiorp=0
menorp=0
for a in range (1,6):
    print('{} {}° pessoa {}'.format('='*5,a,'='*5))
    nome = input('Qual o seu nome: ')
    idade = int(input('Escreva a sua idade: '))
    peso = float(input('Escreva o seu peso:'))
    sexo = input('Sexo [M/F]: ').strip().upper()
    #Mulheres com menos de 20 anos
    if sexo == 'F':
        if idade >= 20:
            tot += +1
    #média de idade
    contador += +1
    media += idade
    final= media/contador
    #O mais velho e mais novo
    if a == 1:
        maior=idade
        menor=idade
        mnome=nome
        mnnome=nome
    elif idade > maior:
        maior=idade
        mnome=nome
    elif idade < menor:
        menor=idade
        mnnome=nome
    #O maior e menor peso
    if a == 1:
        maiorp=peso
        menorp=peso
    elif peso > maiorp:
        maiorp=peso
    elif peso < menorp:
        menorp=peso

print("a média de idade do grupo foi:",final)
print('O maior idade foi {} {} e a menor idade foi {} {}'.format(mnome,maior,mnnome,menor))
print('São ao todo {} mulheres com mais de 20 anos'.format(tot))
print('O maior peso foi de {} Kg e o o menor peso foi de {} Kg'.format(maiorp,menorp))