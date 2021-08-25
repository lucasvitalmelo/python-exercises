# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome: ')).strip().lower()
n = nome.split()
print(n[0])
print(n[len(n)-1])