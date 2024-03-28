# Conta o número de idades maiores ou iguais a 18 de 10 anos de nascimento digitados pelo usuário

cont = 1
num = 0
while cont <= 10:
    idade = int(input('Digite o ano de nascimento: '))
    maior = 2021 - idade 
    if maior >= 18: 
        num += 1
    cont += 1
print (f'{num} pessoas são maiores de idade.')