# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

print('========================================')

num  = int(input("Digite um número: "))

unidade = num // 1 % 10
dezena = num // 10 % 10
centeza = num // 100 % 10
milhar = num // 1000 % 10

print('unidade: {}'.format(unidade))
print('dezena: {}'.format(dezena))
print('centeza: {}'.format(centeza))
print('milhar: {}'.format(milhar))

print('========================================')

