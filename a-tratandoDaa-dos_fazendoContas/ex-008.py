# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = int(input("Digite um número: "))

cm = m * 100

mm = m * 1000

print("{} metros contém {} centimeros.".format(m, cm))
print("{} metros contém {} milimetros.".format(m, mm))
