soma=0
int=0
for c in range(1,501,2):
    if c % 3 == 0:
        int += +1
        soma += c
print(soma,int)