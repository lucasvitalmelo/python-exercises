# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
print('')
print( '-' * 50 )
gamer = int(input("Qual o número de 0 à 9 que a maquina pensou? :"))

cpu = randint(0, 9)

print("\nTAM TAM TAM TAM...\n")

sleep(3)

if gamer == cpu:
  print(" \o/ ACERTOU , o numero era {} e vc disse {}".format(cpu, gamer))
else:
  print(" :( ERROU , o numero era {} e vc disse {}".format(cpu, gamer))

print("\n*-----------------------------------------------------------*")
