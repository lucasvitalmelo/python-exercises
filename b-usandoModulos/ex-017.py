# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.
from math import hypot

print("\n------------------------------------------\n")

catOposto = float(input("Digite o cateto oposto: "))

catAdjacente = float(input("\nDigite o cateto adjacente: "))

hipotenusa = hypot(catOposto, catAdjacente)
print("\n------------------------------------------")
print("A hipotenusa é: {:.2f}".format(hipotenusa))
print("------------------------------------------")
