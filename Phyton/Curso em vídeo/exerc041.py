from datetime import date
a=date.today().year
b=int(input("Data de nascimento:"))
c=a-b
print('O Atleta possuí {} anos, então ele é'.format(c))
if c < 9:
    print("nadador mirim")
elif c >= 9 and c < 14:
    print('Nadador infatil')
elif c >= 14 and c < 19:
    print("Nadador Junior")
elif c >= 19 and c < 25:
    print("Nadador sênior")
elif c >= 25:
    print('Nadador Master')