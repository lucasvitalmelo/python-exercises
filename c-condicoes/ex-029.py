# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input("\nVelocidade do carro: "))

if velocidade <= 80:
  print('Tenha um bom dia!')
else:
  print('\n---------------MULTA DE VELOCIDADE---------------')
  print('Você ultrapassou o limite de velocidade de 80Km/h \n')
  print('Valor da Multa = R${:.2f}'.format((velocidade - 80) * 7))
