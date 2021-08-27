# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
print("\n------------------------------------------------------------------\n")

salario = float(input("Digite o salario: "))
print("")
aumento = salario * (15/100)

print("O salario de R${} com aumento de 15% ficara por R${:.2f}.".format(salario, salario+aumento))

print("\n------------------------------------------------------------------\n")
