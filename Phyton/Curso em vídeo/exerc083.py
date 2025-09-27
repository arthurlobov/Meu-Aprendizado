expressao=[]
cont=exp=0
expressao.append(input('Digite uma expressão:'))
for d in expressao:
    if d == '(':
        cont+=1
    elif d==')':
        exp+=1
if exp+cont==0:
    print('verdadeiro')
else:
    print('falso')