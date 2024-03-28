# Código de adição de 5% de desconto a um valor digitado pelo usuário

valor = float(input("Digite o valor: "))
porc = valor * 5/100
desc = valor - porc
print (f"5% de desconto no valor R${valor} é R${desc}.\n")
print ("Programa encerrado")