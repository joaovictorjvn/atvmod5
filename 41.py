import sys
peso = float(input("Informe o seu peso em Kg: "))
alt = float(input("Informe a sua altura em metros: "))
if peso <= 0 or alt <= 0:
    sys.exit("Dados Inválidos")
imc = peso / (alt * alt)
if imc <= 18.5:
    print("Seu IMC indica que você está abaixo do peso.")
elif imc <= 24.9 >= 18.6:
    print("Seu IMC indica que você está no peso ideal, saudável.")
elif imc <= 29.9 > 24.9:
    print("Seu IMC indica que você está com peso em excesso, acima do peso.")
elif imc <= 34.9 > 29.9:
    print("Seu IMC indica que você está com obesidade de grau 1.")
elif imc <= 39.9 > 34.9:
    print("Seu IMC indica que você está com obesidade de grau 2(Severa).")
elif imc >= 40:
    print("Seu IMC indica que você está com obesidade de grau 3(Mórbida).")
