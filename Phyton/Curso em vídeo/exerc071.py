print('='*30)
print('Banco')
print('='*30)
v=float(input('Qual valor você deseja sacar?'))
s5=v//50
s50=v%50
x=v-50*s5
if s50 != 0:
    s10=x//10
    y=x-s10*10
    if s10 != 0:
        s1=y//1
print(f'''No total foram {s5} notas de 50RS
total de {s10} notas de 10 RS
total de {s1} notas de 1 RS''')