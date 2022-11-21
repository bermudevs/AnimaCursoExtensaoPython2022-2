#criar funções

preco = 2899.21

#calculo 5%, quarda variável e exibe

imposto = preco*0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#criar função calcular_imposto() que calcular um imposto de 5% e retorna a quem pediu

#declaração da função(como funciona)
def calcular_imposto(preco_item):
  imposto = preco_item * 0.07
  return imposto

#Aqui é o uso... aqui é o imposto a calcular...
preco = 485
imposto = calcular_imposto(preco) #o retur da linha 19 que manda pra cá a info novamente
print(f"esse aqui é com a função (7%):{imposto}")
print("")

#agora a alíquota é 7#

valores = [1.99, 22.30, 59.90, 1929.50]

for valor in valores:
  print(f"o imposto de {valor} é {calcular_imposto(valor)}")

#declarar função calcular_imposto_aliquota que recebe dois parametros

def calcular_imposto_aliquota(valor, aliquota=7):
  imposto = valor * aliquota / 100
  return imposto

for valor in valores:
  print(f"o imposto de {valor} é {calcular_imposto(valor)}")

# imposto a 10%
for valor in valores:
  print(f"o imposto de {valor} é {calcular_imposto_aliquota(valor, 10)}")