# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input("\n\nDigite um qualquer número: "))

result = n % 2

if result == 0:
  print("\nO número {} é PAR.".format(n))
else:
  print("\nO número {} é ÍMPAR.".format(n))