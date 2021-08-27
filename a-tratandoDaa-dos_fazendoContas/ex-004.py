# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

caixa = input("Digite algo: ")

print("O tipo primitivo desse valor é ",type(caixa))
print("Só tem espaços? ", caixa.isspace())
print("É um número? ", caixa.isnumeric())
print("É alfabético? ", caixa.isalpha())
print("É alfanumérico ", caixa.isalnum())
print("Está em minusculas? ", caixa.islower())
print("Está em maiusculas? ", caixa.isupper())
print("Está capitalizada? ", caixa.istitle())