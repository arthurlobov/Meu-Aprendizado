expressao=[]
pilha=[]
expressao.append(input('Digite uma expressão:'))
for digito in expressao:
    if digito == '(':
        pilha.append('(')
    elif digito == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Expressão verdadeira')
else:
    print('expressão inexistente')