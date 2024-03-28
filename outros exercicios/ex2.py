# Se um número for ímpar ele calcula a soma de dois números, se for par calcula o produto

val1 = int(input("Digite um valor: "))
val2 = int(input("Digite outro valor: "))
resto = val1 % 2
if resto == 1:
    soma = val1 + val2
    print(soma)
else:
    produto = val1 * val2
    print(produto)