# Crie um programa que leia o nome completo de uma pessoae mostre:
# - O nome com todas as letras maiuscula
# - O nome com todas minusculas
# - Quantas letras ao todo (sem considerar os espaços)
# - Quantas lestras tem o pirmeiro nome.
print ('--------------------------------------------------------------------------------')
name = str(input("Digite o nome completo: ")).strip()

countLetters = len(name.replace(" ", ""))
countFirstPosition = len(name.split()[0])


print(" O nome com todas as letras maiuscula : {}.\n O nome com todas minusculas : {}.\n Quantas letras ao todo (sem considerar os espaços) : {}. \n Quantas lestras tem o pirmeiro nome : {}.".format(name.upper(), name.lower(), countLetters, countFirstPosition))

print ('--------------------------------------------------------------------------------')