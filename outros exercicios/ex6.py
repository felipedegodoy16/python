# Cálculo de uma PG

razao = int(input("Digite a razão da PG: "))
termo = int(input("Digite o primeiro termo da PG: "))
cont = 1
termos = termo
while cont <= 5:
    termos = razao * termos
    cont = cont + 1
    print(termos)