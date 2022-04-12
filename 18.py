op = int(input("Informe a opção desejada:\n"
               "1 - Soma\n"
               "2 - Subtração\n"
               "3 - Multiplicação\n"
               "4 - Divisão\n"))
if op == 1:
    num1 = int(input("Informe o primeiro número para a operação: "))
    num2 = int(input("Informe o segundo número para a operação: "))
    print(f'A soma dos números inseridos equivale a {num1 + num2}')
elif op == 2:
    num1 = int(input("Informe o primeiro número para a operação: "))
    num2 = int(input("Informe o segundo número para a operação: "))
    print(f'A subtração dos números inseridos equivale a {num1 - num2}')
elif op == 3:
    num1 = int(input("Informe o primeiro número para a operação: "))
    num2 = int(input("Informe o segundo número para a operação: "))
    print(f'A multiplicação dos números inseridos equivale a {num1 * num2}')
elif op == 4:
    num1 = int(input("Informe o primeiro número para a operação: "))
    num2 = int(input("Informe o segundo número para a operação: "))
    print(f'A divisão dos números inseridos equivale a {num1 / num2}')
else:
    print("Opção inválida.")
