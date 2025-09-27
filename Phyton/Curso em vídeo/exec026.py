from itertools import count
palavra=input('digite uma frase:').strip().upper()
c=palavra.count('O')
posiçãoinicial = palavra.find('O')
print('Sua frase possuí {} o'.format(c))
print('A letra o aparece inicialmente na posição {}'.format(posiçãoinicial+1))
final=palavra.rfind('O')
print('A ultima letra o aparece na posição {}'.format(final+1))

