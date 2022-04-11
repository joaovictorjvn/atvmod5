num = int(input("Informe um número: "))
if num > 0:
    res = [int(a) for a in str(num)]
    tam = len(res) - 1
    i = 0
    aux = 0
    while i <= tam:
        if i == tam:
            tot = res[i] + aux
            break
        else:
            tot = res[i] + res[i + 1]
            aux = aux + tot
            i = i + 2
    print(f'A soma dos algorismos é {tot}')
else:
    print("Número inválido")
