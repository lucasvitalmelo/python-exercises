# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

lista = ["Lucas", "Raquel", "Camila", "Marcela", "Jacqueline", "Esmeraldino"]

sorteio = choice(lista)

print("\n______________________{}______________________\n".format(sorteio))