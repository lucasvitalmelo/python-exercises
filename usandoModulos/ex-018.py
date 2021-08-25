#  Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

print("\n--------------------------------------------\n")

an = int(input("Digite o angulo que deseja calcular: "))

rad = radians(an)

sine = sin(rad)
cosine = cos(rad)
tangent = tan(rad)

print("\n--------------------------------------------\n")

print("O angulo de {}° tem o Seno de {:.2f}".format(an, sine))
print("O angulo de {}° tem o Cosseno de {:.2f}".format(an, cosine))
print("O angulo de {}° tem o Tangente de {:.2f}".format(an, tangent))

print("\n--------------------------------------------\n")
