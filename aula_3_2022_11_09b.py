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
  imposto = preco_item * 0.05
  return imposto

#Aqui é o uso... aqui é o imposto a calcular...
preco = 485
imposto = calcular_imposto(preco) #o retur da linha 19 que manda pra cá a info novamente
print(imposto)
