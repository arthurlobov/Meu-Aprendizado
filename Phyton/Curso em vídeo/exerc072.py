a = int(input('escreva um número entre 0 e 20:'))
while a > 20:
    a=int(input('escreva um número entre 0 e 20:'))
b= ('zero','um','dois','tres', 'quatro','cinco','seis','sete','oito',
    'nove','dez','onze','doze','treze','quatorze','quinze','dezesseis',
    'dezessete','dezoito','dezenove','vinte','trinta')
c=b[a]
print(c)