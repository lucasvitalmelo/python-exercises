# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
print("\n----------------------------------------------------------\n")
valor = float(input("Digite o valor do protudo para receber o desconto: "))

desconto = valor * (5/100)
print("\n----------------------------------------------------------")
print("R${} com desconto de 5% é de R${:.2f}".format(valor, valor-desconto))
print("----------------------------------------------------------")
