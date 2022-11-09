# comando input(): permissão usuário digite algo
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

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

