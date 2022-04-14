alt = float(input("Informe a altura em metros: "))
pes = float(input("Informe o peso em quilogramas: "))
if alt <= 1.20:
    if pes <= 60:
        print("Esse indivíduo pertenece a categoria 'A'.")
    elif pes > 60 and not pes > 90:
        print("Esse indivíduo pertenece a categoria 'D'.")
    elif pes > 90:
        print("Esse indivíduo pertenece a categoria 'G'.")
elif alt > 1.20 and not alt > 1.70:
    if pes <= 60:
        print("Esse indivíduo pertenece a categoria 'B'.")
    elif pes > 60 and not pes > 90:
        print("Esse indivíduo pertenece a categoria 'E'.")
    elif pes > 90:
        print("Esse indivíduo pertenece a categoria 'H'.")
elif alt > 1.70:
    if pes <= 60:
        print("Esse indivíduo pertenece a categoria 'C'.")
    elif pes > 60 and not pes > 90:
        print("Esse indivíduo pertenece a categoria 'F'.")
    elif pes > 90:
        print("Esse indivíduo pertenece a categoria 'I'.")


"""elif alt >= 1.20 <= 1.70 and pes < 60:
    print("Esse indivíduo pertenece a categoria 'B'.")
elif alt >= 1.20 >= 1.70 and pes >= 60 <= 90:
    print("Esse indivíduo pertenece a categoria 'E'.")
elif alt >= 1.20 >= 1.70 and pes > 90:
    print("Esse indivíduo pertenece a categoria 'H'.")
elif alt > 1.70 and pes < 60:
    print("Esse indivíduo pertenece a categoria 'C'.")
elif alt > 1.70 and pes >= 60 <= 90:
    print("Esse indivíduo pertenece a categoria 'F'.")
elif alt > 1.70 and pes > 90:
    print("Esse indivíduo pertenece a categoria 'I'.")"""
