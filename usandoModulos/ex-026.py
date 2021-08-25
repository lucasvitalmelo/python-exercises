# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().lower()

print('Quantas vezes aparece a letra “A”: ', frase.count('a'))
print('Em que posição ela aparece a primeira vez: ',frase.find('a') + 1)
print('Em que posição ela aparece a última vez: ', frase.rfind('a') + 1)