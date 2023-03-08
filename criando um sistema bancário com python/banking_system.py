# Desafio de projeto DIO - Curso Python Developer - Módulo Fundamentos

##  v1 - Criar um sistema bancário em python com as opções de saque, depósito e visualizar extrato bancário e um usuário

# REGRAS:
## DEPÓSITO: TODOS OS DEPÓSITOS DEVEM SER ARMAZENADOS E EXIBIDOS NO EXTRATO
## SAQUE: LIMITE DE 3 SAQUES DIÁRIOS COM LIMITE DE VALOR DE R$500,00 POR SAQUE, CASO NÃO HAJA SALDO DISPONÍVEL DEVE-SE INFORMAR A FALTA DE SALDO, TODOS OS SAQUES DEVEM SER ARMAZENADOS E EXIBIDOS NO EXTRATO
## EXTRATO: DEVE EXIBIR O VALOR ATUAL EM CONTA, TODOS OS VALORES SACADOS E DEPOSITADOS NO FORMATO R$xxx.xx




# variáveis
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

valor = 0
saldo = 0
limite_diario = 500
total_saques = 0
num_saques = 0
LIMITE_SAQUES = 3

extrato = """"""


## Código
import os
while True:

    opcao = input(menu)
    os.system("cls") or None

    if opcao == "d":
        valor = float(input("Digite o valor que deseja depositar:  "))
        if valor > 0:
            saldo += valor
            extrato += f"""R${valor:.2f} C \n"""
        else:
            print("Falha, digite um valor válido!")

    elif opcao == "s":
        if num_saques < LIMITE_SAQUES:
            valor = float(input("Digite o valor do saque:  "))
            if valor > limite_diario or valor > saldo or total_saques + valor >= limite_diario + 1:
                print("Saque não autorizado")
            else:    
                saldo -= valor
                extrato += f"""R${valor:.2f} D \n"""
                num_saques += 1
                total_saques += valor
                print(f"valor retirado: R${valor:.2f}")
        else:
            print("Limite de Saques excedido!!")

    elif opcao == "e":
        print(f"*************** EXTRATO *****************\n")
        print(f"Seu Saldo atual é de R${saldo:.2f}\n")        
        print(f"{extrato}\n")
        

    elif opcao == "q":
        print("Volte sempre!!\n")
        break

    else:
        print("Selecione uma opção válida")