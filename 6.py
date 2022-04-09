num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
if num1 > num2:
    print(f'O maior número é {num1} com uma diferença de {num1 - num2} para {num2}')
else:
    print(f'O maior número é {num2} com uma diferença de {num2 - num1} para {num1}')
