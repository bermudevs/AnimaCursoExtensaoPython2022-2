# comando input(): permissão usuário digite algo
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
genero = input("Coloque M para Masculino ou F para Feminino")


# comando de saída... exibir na tela
print("Seja bem vindo, {}! Sua idade é {} anos".format (nome,idade))

# mostrar o dobro da idade
'''
poderia colocar em uma variável o dobro
mas fiz direto no print
exemplo
dobro = idade * 2
tive que converter a idade em número inteiro
lá na atribuição da variável
'''  
print("Daqui {} anos, você terá {} anos".format (idade,idade*2))

#Estrutura condicional (if)
#Se a idade for maior que 18, mostre uma mensagem.
if idade >= 18:
  print("Você é maior de idade, lega! Já pode beber e dirigir, nunca os dois juntos.")
else:
  print("você, agora não é maior de idade, mas em breve, aos 18 anos, poderá dirigir e beber, nunca os dois juntos.")

if idade >= 18 and genero == "M":
  print("... e você também precisa/precisou prestar serviço militar obrigatório")