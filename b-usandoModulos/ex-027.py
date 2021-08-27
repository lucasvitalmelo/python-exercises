# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome: ')).strip().lower()

n = nome.split()

print("Seu primeiro nome é: ",n[0])

print('Seu ultimo nome é: ', n[len(n)-1])