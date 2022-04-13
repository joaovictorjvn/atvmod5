an = int(input("Informe o ano desejado: "))
if an % 400 == 0 or an % 4 == 0 and not an % 100 == 0:
    print("O ano inserido é bissexto.")
else:
    print("O ano inserido não é bissexto.")
