#while // enquanto *** você define onde para//
#for // para cada *** [0, 1, 2, 3] // 

# numero = int(input("Digite: "))


# for i in range(1,11):
#   conta = i * numero

#   print(i,'x', numero,'=', conta)
  
# contador = 0
# while True:
#   contador = contador + 1
#   conta = numero * contador

#   if contador >= 10:
#     break

#   if conta % 2 == 0:
#     continue
  
#   print(conta)


# pessoas = ["Lucas", "Cleyson", "Bruno", "Luigi"]


# for index, pessoa in enumerate(pessoas):
#   print("Esse é o valor:", pessoa)
#   print("Essa é a posição", index)


# faça um program que receba 4 notas e mostre a média
# deve ser feito com lista
# equação // soma das notas / pelo tamanho da lista

# somaDasNotas = 0

# for i in range(4):
#   somaDasNotas += float(input("Nota: "))


# media = soma / 4
# print(media)

# notas = []

# from random import randint

# numAleatorio = randint(1, 100)

# print(numAleatorio)

# for i in range(numAleatorio):
#   nota = randint(1, 100)
#   notas.append(nota)
#   print(nota)


# tamanhoNotas = len(notas)
# soma = sum(notas)

# print(soma / tamanhoNotas)




from random import randint
mega = []


for i in range(6):
  num = randint(1, 100)
  
  while num in mega:
    num = randint(1, 100)
  
  mega.append(num)

print(mega)

