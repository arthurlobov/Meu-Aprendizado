lista=[]
for a in range(0,5):
    b=(int(input('Digite um valor: ')))
    if a ==0 or b>lista[len(lista)-1]:
        lista.append(b)
    else:
        pos=0
        while pos < len(lista):
            if b <= lista[pos]:
                lista.insert(pos,b)
                break
            pos+=1

print(lista)