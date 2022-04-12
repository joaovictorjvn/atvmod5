num = int(input("Informe um número: "))
if num % 3 == 0 and not num % 5 == 0:
    print(f'O número {num} é divisível por 3.')
elif num % 5 == 0 and not num % 3 == 0:
    print(f'O número {num} é divisível por 5.')
else:
    print("O número não é divisível por 3 e nem por 5 ou é divisível por ambos, o programa não permite identifcar"
          "tais números.")
