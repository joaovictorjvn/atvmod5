num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))
if num1 >= num2 >= num3:
    print(f'A ordem crescente dos números é {num3}, {num2}, {num1}')
elif num2 >= num1 >= num3:
    print(f'A ordem crescente dos números é {num3}, {num1}, {num2}')
elif num1 >= num3 >= num2:
    print(f'A ordem crescente dos números é {num2}, {num3}, {num1}')
elif num2 >= num3 >= num1:
    print(f'A ordem crescente dos números é {num1}, {num3}, {num2}')
elif num3 >= num1 >= num2:
    print(f'A ordem crescente dos números é {num2}, {num1}, {num3}')
elif num3 >= num2 >= num1:
    print(f'A ordem crescente dos números é {num1}, {num2}, {num3}')
