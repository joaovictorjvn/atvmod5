val1 = float(input("Informe o primeiro valor: "))
val2 = float(input("Informe o segundo valor: "))
val3 = float(input("Informe o terceiro valor: "))
op = int(input("Informe a média desejada: \n"
               "1 - Geométrica\n"
               "2 - Ponderada\n"
               "3 - Harmônica\n"
               "4 - Aritmética\n"))
if op == 1:
    print(f'A média geométrica dos valores equivale a {(val1 * val2 * val3) ** (1 / 3)}')
elif op == 2:
    print(f'A média ponderada dos valores equivale a {(val1 + (val2 * 2) + (val3 * 3)) / 6}\n('
          f'O primeiro valor recebeu peso 1, o segundo valor recebeu peso 2 \ne'
          f'o terceiro valor recebeu peso 3).')
elif op == 3:
    print(f'A média harmônica dos valores equivale a {1 / ((1 / val1) + (1 / val2) + (1 / val3))}')
elif op == 4:
    print(f'A média aritmética dos valores equivale a {(val1 + val2 + val3) / 3}')
else:
    print("Opção Inválida.")
