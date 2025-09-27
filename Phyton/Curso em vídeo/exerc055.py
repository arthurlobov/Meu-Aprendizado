maior=0
menor=0
for a in range (1,6):
    peso = float(input('Qual a seu peso: '))
    if a == 1:
        maior=peso
        menor=peso
    if peso > maior:
        maior=peso
    if menor > peso:
        menor=peso
print(maior,menor)