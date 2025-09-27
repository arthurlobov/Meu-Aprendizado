cont=c=s=a=0
while True:
    a=int(input('Qual o número você deseja: '))
    if a == 999:
        break
    s+=a
    cont+=1
print(f'a soma dos valores foi {s} e o total de números foi {cont}')