from time import sleep
#função
def maior(*num):
    m=0
    print('-'*30)
    print(f'analisando....',end='')
    for e in range(0,len(num)):
        if num[e] >= m:
            m=num[e]
        print(f' {num[e]}',end='')
        sleep(0.5)
    print(f'\nForam informados {len(num)} valores ao todo')
    print(f'O maior valor é o {m}')


#teste
maior(2,4,5,6)
maior(3,4,5,1,2,)
maior(2)
maior(0)