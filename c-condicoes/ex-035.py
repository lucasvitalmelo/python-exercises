# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('\n--------Insira 3 valores para descobrir se eles formam um Triangulo--------\n\n')

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

print('')
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
  print("Verdadeiro")
else:
 print("Falso")