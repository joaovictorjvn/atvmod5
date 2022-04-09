sal = float(input("Informe o salário do trabalhador: R$ "))
prest = float(input("Informe o valor da prestação do empréstimo: R$ "))
if prest > sal * 0.2:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")
