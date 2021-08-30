# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

print('')
salario = float(input("Salário: "))
print('')

if salario <= 1250.00:
  newValue = (salario*15)/100 

else:
  newValue = (salario*10)/100

print('Salario antigo: {:.2f}\nSalario depois do Aumento: R${:.2f}'.format(salario, salario + newValue))