# Código simples de acréscimo de 12% a um valor digitado pelo usuário

valor = float(input("Digite o valor: "))
acres = (valor * 12/100) + valor
print (f"12% de acréscimo no valor R${valor} é R${acres}.\n")
print ("Programa encerrado")