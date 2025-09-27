import random
Aluno1=input("nome do aluno: ")
Aluno2=input("nome do aluno: ")
Aluno3=input("nome do aluno: ")
Aluno4=input("nome do aluno: ")
lista=[Aluno1,Aluno2,Aluno3,Aluno4]
random.shuffle(lista)
print('a ordem escolhida foi',lista)