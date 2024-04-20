menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
 
=> """

saldo = 0
limite_saque_saldo = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Digite o valor que deseja depositar: "))
        if deposito <= 0:
            print("Depósito inválido, precisa ser um valor positivo! Digite novamente!")
        else:
            saldo += deposito
            print("O novo saldo é: R$", saldo)
            extrato += f"Depósito R$ {deposito:.2f}\n"
      

    elif opcao == "2":
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        saque = float(input("Digite o valor que deseja sacar: "))
        
        if excedeu_saques:
            print("Limite de saques diários atingido. Volte novamente amanhã, tenha um bom dia!")
        elif saque < saldo:
            if saque > 500:
                print("Saque inválido, o limite de saque é R$ 500.00")
            elif saque > 0:    
                saldo -= saque
                print("Saque feito com sucesso! O seu novo saldo é: R$", saldo)
                extrato += f"Saldo R$ {saldo:.2f}\n"
                numero_saques += 1
            else:
                print("Saque inválido, digite um valor positivo!")    
        
        else:
            print("Você não possui saldo suficiente, seu saldo atual é: R$", saldo)
                          
    elif opcao == "3":
        print("\n ******* Olá, veja o seu extrato diário *******")
        print("\n Não ocorreram movimentações hoje." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("\n **********************************************")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, selecione novamente!")            

