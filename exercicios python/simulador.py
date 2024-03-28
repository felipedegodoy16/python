# Código de um simulador de investimentos

while True:
    print("-------------------------------")
    print("  Seja bem-vindo(a) ao Mybank  ")
    print("   SIMULADOR DE INVESTIMENTO   ")
    print("-------------------------------")

    # escolhendo a opção
    print("Títulos disponíveis:")
    print("1 - Tesouro Prefixado 2024")
    print("2 - Tesouro Prefixado 2026")

    #calculando o investimento
    titulo = int(input("Qual título você gostaria de fazer uma simulação?: "))

    val_ir = 0
    meses_1 = 32
    meses_2 = 50

    val_investido = float(input("\n Qual o valor você quer investir?: "))
    aporte = float(input("Se você for investir todo mês, qual o valor?: "))

    # título 1
    if titulo == 1:
        total_investido = aporte * meses_1 + val_investido

        # calculando valor bruto
        rentabilidade = total_investido * 12.38/100
        b3 = total_investido * 0.25/100
        val_bruto = total_investido + rentabilidade + b3

        # imposto de 7,5%
        if val_bruto > 1903.98 and val_bruto < 2826.66:
            ir = val_bruto * 0.75/100
            val_ir = val_bruto + ir

        # imposto de 15%
        elif val_bruto > 2826.65 and val_bruto < 3751.06:
            ir = val_bruto * 1.5/100
            val_ir = val_bruto + ir
        
        # imposto de 22,5%
        elif val_bruto > 3751.05 and val_bruto < 4664.69:
            ir = val_bruto * 2.25/100
            val_ir = val_bruto + ir

        # imposto de 27,5%
        elif val_bruto > 4664.68:
            ir = val_bruto * 2.75/100
            val_ir = val_bruto + ir
        
        #calculando o valor líquido
        val_liquido = val_ir - ir - b3

    # título 2
    else: 
        total_investido = aporte * meses_2 + val_investido

        # calculando valor bruto
        rentabilidade = total_investido * 12.30/100
        b3 = total_investido * 0.25/100
        val_bruto = total_investido + rentabilidade + b3

        # imposto de 7,5%
        if val_bruto > 1903.98 and val_bruto < 2826.66:
            ir = val_bruto * 0.75/100
            val_ir = val_bruto + ir

        # imposto de 15%
        elif val_bruto > 2826.65 and val_bruto < 3751.06:
            ir = val_bruto * 1.5/100
            val_ir = val_bruto + ir
        
        # imposto de 22,5%
        elif val_bruto > 3751.05 and val_bruto < 4664.69:
            ir = val_bruto * 2.25/100
            val_ir = val_bruto + ir

        # imposto de 27,5%
        elif val_bruto > 4664.68:
            ir = val_bruto * 2.75/100
            val_ir = val_bruto + ir
        
        #calculando o valor líquido
        val_liquido = val_ir - ir - b3

    # resultado da simulação
    print("------------------------------")
    print("    RESULTADO DA SIMULAÇÃO    ")
    print("------------------------------")
    print(f"Valor inicial investido: {val_investido}")
    if titulo == 1:
        print(f"Aportes de {aporte}  por {meses_1} meses")
    else:
        print(f"Aportes de {aporte}  por {meses_2} meses")
    print(f"Valor total investido {total_investido}")
    print("------------------------------")
    print(f"Valor bruto: {val_ir}")
    print(f"I.R.: {ir}")
    print(f"Taxa da B3: {b3}")
    print(f"Valor líquido: {val_liquido}")
    print("------------------------------")

    opcao = str(input("\n Quer continuar a simulação? [s/n]: "))
    if opcao == 'n':
        break
    print("Programa encerrado")