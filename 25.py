a = float(input("Informe o valor que acompanha x²(a): "))
b = float(input("Informe o valor que acompanha x (b): "))
c = float(input("Informe o valor de c(Não acompanha x diretamente): "))
if b ** 2 - 4 * a * c < 0:
    print("Não existe raíz real.")
elif b ** 2 - 4 * a * c == 0:
    print(f'Raíz única equivalente a {(-b) / (2 * a)}')
else:
    print(f'A primeira raíz é {((-b) + ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)}\n'
          f'A segunda raíz é {((-b) - ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)}')
