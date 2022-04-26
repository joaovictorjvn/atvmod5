sal = float(input("Informe o salário do funcionário: "))
ant = int(input("Informe o tempo de trabalho em anos do funcionário(use 0 caso tenha chegado a um ano ainda): "))
if sal <= 500 and ant < 1:
    print(f'O novo salário do funcionário é R$ {sal + (sal * 0.25)}, o salário sofreu um reajuste de R$ {sal * 0.25}'
          f' equivalente a 25%, sem direito a bônus.')
elif sal <= 1000 > 500 and ant <= 3 >= 1:
    print(f'O novo salário do funcionário é R$ {sal + (sal * 0.20) + 100}, o salário sofreu um reajuste de R$ '
          f'{sal * 0.20} equivalente a 20%, com direito a R$ 100.00 de bônus.')
elif sal <= 1500 > 1000 and ant <= 6 > 3:
    print(f'O novo salário do funcionário é R$ {sal + (sal * 0.15) + 200}, o salário sofreu um reajuste de R$ '
          f'{sal * 0.15} equivalente a 15%, com direito a R$ 200.00 de bônus.')
elif sal <= 2000 > 1500 and ant <= 10 > 6:
    print(f'O novo salário do funcionário é R$ {sal + (sal * 0.10) + 300}, o salário sofreu um reajuste de R$ '
          f'{sal * 0.10} equivalente a 10%, com direito a R$ 300.00 de bônus.')
elif sal > 2000 and ant > 10:
    print(f'O novo salário do funcionário é R$ {sal + 500}, o salário não sofreu reajuste,'
          f' mas recebe o um bônus de R$ 500.')
else:
    print("O salário do funcionário não sofrerá nenhuma alteração.")
