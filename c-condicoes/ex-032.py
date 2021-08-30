# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date 
print('')
data = int(input("Que ano deseja analisar ? isira 0 para analisar o ano atual: "))
print('')

if data == 0:
  data = date.today().year
if data % 4 == 0 and data % 100 != 0 or data % 400 == 0:
  print("{} é bissexto".format(data))
else:
  print("{} não é bissexto".format(data))