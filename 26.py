dis = float(input("Informe a distâcia percorrida em Km: "))
comb = float(input("Informe quantos litros de combustível foram utilizados para precorrer a distância mencionada "
                   "anteriormente: "))
if dis / comb <= 8:
    print("Venda o carro!")
elif dis / comb > 8 and not dis / comb > 12:
    print("Econômico!")
elif dis / comb > 12:
    print("Super Econômico!")
"""
No enunciado está dito entre 8 e 14 (segundo elif), aqui foi utilizado 12 pois se esse valor estiver
orreto não haveria necessidade da categoria seguinte.
"""
