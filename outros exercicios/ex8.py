media = int(input("Digite a sua média: "))
frequencia = int(input("Digite a sua frequência: "))
if frequencia < 75:
    print("Você foi reprovado!")
elif media < 7:
    print("Você está de recuperação!")
else:
    print("Você foi aprovado!")