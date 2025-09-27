print('='* 10,'Loja do Arthur','='*10)
a=float(input('Qual o preço do produto? RS '))
print('''Qual a forma de pagamento
[1] á vista / dinheiro ou cheque
[2] á vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
b=int(input('Opção:'))

if b == 1:
    c=a*0.9
    d=a*0.1
    print(' O preço do seu produto sai de RS {:.2f}, e fica por apenas RS {:.2f}, totalizando um desconto de RS {:.2f}'.format(a,c,d))
elif b == 2:
    e=a*0.95
    f=a*0.05
    print('Se seu pagamento for á vista no cartão  saí de RS', a, 'para RS', e, 'totalizando um desconto de RS',f)
elif b == 3:
    print('Sua compra sai por {:.2f}'.format(a))
elif b == 4:
    g= a*1.20
    h=a*0.20
    print('O seu produto sofre um aumento de RS {:.2f}, totalizando o valor de RS {:.2f}'.format(h,g))