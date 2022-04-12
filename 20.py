val1 = float(input("Informe o primeiro valor: "))
val2 = float(input("Informe o segundo valor: "))
val3 = float(input("Informe o terceiro valor: "))
if val1 > val2 + val3 or val2 > val1 + val3 or val3 > val1 + val2:
    print("Os valores inseridos não podem ser os lados de um triângulo.")
else:
    if val1 == val2 == val3:
        print("Os valores inseridos podem ser os lados de um triângulo, sendo un triângulo equilátero(Aquele que possui"
              "três lados iguais).")
    elif val1 == val2 != val3 or val1 == val3 != val2 or val2 == val3 != val1:
        print("Os valores inseridos podem ser os lados de um triângulo, sendo un triângulo isósceles(Aquele que possui"
              "apenas dois lados iguais).")
    else:
        print("Os valores inseridos podem ser os lados de um triângulo, sendo un triângulo escaleno(Aquele que possui"
              "três lados diferentes).")
