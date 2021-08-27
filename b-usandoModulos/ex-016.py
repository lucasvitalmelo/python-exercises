# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

print("\n\---------returns the integer value----------/\n")

n = float(input("Enter a value: "))

value = trunc(n)

print("\n The value integer is: ", value)

print("\n*---------End----------*\n")
