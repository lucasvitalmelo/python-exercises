# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input("Digite um número: "))

double = 2 * n

triple = 3 * n

squareRoot = n ** 0.5

print("O dobro {} de vale {}".format(n, double))
print("O tripo de {} vele {}".format(n, triple))
print("A raiz quadrada de {} vele {:.2f}".format(n, squareRoot))