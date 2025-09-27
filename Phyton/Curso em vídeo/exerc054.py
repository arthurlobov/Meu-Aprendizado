from datetime import date
dat=date.today().year
data=int(dat)
idadec=0
idadecc=0
for ler in range(1,8):
    ano = int(input('A {}° data de nascimento: '.format(ler)))
    idade = data - ano
    if idade >= 18:
        idadec += 1
    else:
        idadecc += 1
print('Este grupo possuí {} maiores de idade e {} menores de idade'.format(idadec,idadecc))

