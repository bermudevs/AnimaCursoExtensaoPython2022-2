#Pede o nome do aluno e a nota (0 a 10) nota 10, mostra "Você é monstro!!!"

nome = input("Escreva seu nome ")
nota = float(input("Digite sua nota: "))

if nota == 10:
  print(f"{nome}, você é Monstro!!!")
elif nota >= 6 and nota < 10:
  print(f"{nome}, não foi um 10 mas já valeu")
else:
  print(f"{nome}, se estrepou!")