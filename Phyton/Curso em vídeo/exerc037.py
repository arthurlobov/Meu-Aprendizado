print('Escolha uma das bases para conversão:')
print('[1] Binário')
print('[2] octal')
print('[3] Hexadecimal')
a=int(input(('Sua opção:')))
b = int(input('Digite seu número em decimal:'))

if a == 1:
    print("Seu número é: {}".format(bin(b)[2:]))
elif a == 2:
    print("Seu número é:{}".format(oct(b)[2:]))
elif a ==3:
    print("Seu númeor é:{}".format(hex(a)[2:]))