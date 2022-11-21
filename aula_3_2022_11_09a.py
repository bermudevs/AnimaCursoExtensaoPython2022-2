# regressiva
contador = 10

while(contador >= 1):
  print(contador)
  contador = contador-1
print("")

# progressiva
contador = 1

while(contador <= 10):
  print(contador)
  contador = contador+1

#laço for (python for = for each)
fruta = "morango"
print(fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "pêra"

#lista
frutas = ["morango", "laranja", "pêra"]

#quero exibir apenas a 3 fruta(pêra)
print(frutas[1])

#quantas frutas têm na lista
print(len(frutas))

#quero incluir uma fruta nova
frutas.append("manga")
frutas.append("uva")

print(len(frutas))
print(frutas[3])
print("")


print("FRUTAS EM REPETIÇÃO")
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
print("")

print("FRUTAS DENTRO DO LOOP")
i = 0 #(i de index)
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1
print("")

print("exemplo das frutas com FOR")
for fruta in frutas:
  print(fruta)
  
