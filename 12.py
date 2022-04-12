import math
num = float(input("Informe um número: "))
if num > 0:
    print(f'O logaritmo do número informado é {math.log(num,10)}')
else:
    print("Número inválido.")
