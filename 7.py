num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
if num1 > num2:
    print(f'O maior número é {num1}')
elif num1 == num2:
    print(f'Os números são iguais {num1} e {num2}')
else:
    print(f'O maior número é {num2}')
