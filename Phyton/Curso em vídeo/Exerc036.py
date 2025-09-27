a=int(input("Valor do empréstimo: RS"))
b=int(input("Período de pagamento:"))
c=int(input('Salário: RS'))

x=a/(b*12)
if x >= c*0.3:
    print('Empréstimo Negado')
else:
    print('Empréstimo aprovado')