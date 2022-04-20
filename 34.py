nota = float(input("Informe a nota do aluno: "))
fal = int(input("Informe a quantidade de faltas que o aluno possui: "))
if nota < 0 or nota > 10 or fal < 0:
    print("Dados inválidos inseridos, notas não podem exceder 10.0 como também não podem ser inferiores \n"
          "a 0.0, assim como as faltas, que não podem ser inferiores a 0.")
elif fal <= 20:
    if nota <= 10 >= 9:
        print("O aluno recebeu conceito 'A'.")
    elif nota <= 8.9 >= 7.5:
        print("O aluno recebeu conceito 'B'.")
    elif nota <= 7.4 >= 5.0:
        print("O aluno recebeu conceito 'C'.")
    elif nota <= 4.9 >= 4.0:
        print("O aluno recebeu conceito 'D'.")
    else:
        print("O aluno recebeu conceito 'E'.")
else:
    if nota <= 10 >= 9:
        print("O aluno recebeu conceito 'B'.")
    elif nota <= 8.9 >= 7.5:
        print("O aluno recebeu conceito 'C'.")
    elif nota <= 7.4 >= 5.0:
        print("O aluno recebeu conceito 'D'.")
    else:
        print("O aluno recebeu conceito 'E'.")

"""elif nota <= 10 >= 9 and fal <= 20:
    print("O aluno recebeu conceito 'A'.")
elif nota <= 10 >= 9 and fal > 20 or nota <= 8.9 >= 7.5 and fal <= 20:
    print("O aluno recebeu conceito 'B'.")
elif nota <= 8.9 >= 7.5 and fal > 20 or nota <= 7.4 >= 5.0 and fal <= 20:
    print("O aluno recebeu conceito 'C'.")
elif nota <= 7.4 >= 5.0 and fal > 20 or nota <= 4.9 >= 4.0 and fal <= 20:
    print("O aluno recebeu conceito 'D'.")
else:
    print("O aluno recebeu conceito 'E'.")"""
