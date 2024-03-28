# Estrutura de decisão para verificar o número digitado pelo usuário

valor = int(input("Digite o valor: "))
if valor == 0:
    print ("Número nulo.\n")
elif valor < 0:
    print ("Número negativo.\n") 
else: 
    print ("Número positivo.\n")
print ("Programa encerrado")