# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
print("")
print("---------------------------------------")

cota = float(input("Qual a cotação do dolar hoje? "))
print("")
reais = float(input("Digite o valor a ser convertido: "))

dolar = reais / cota 
print("")
print("-------------------------------")
print("R$ {} pode comprar US$ {:.2f}".format(reais, dolar))

