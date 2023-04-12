# Página das Funções do sistema
import os
import time


# Variáveis
users = dict()
AGENCIA = "0001"
num_conta = 0

# Main/Initial menu
def initial_menu():
    print("""

    *********** Banco GC *************

        Escolha uma opção:

        [1] - Fazer Login
        
        [2] - Criar novo Usuário

        [3] - Sair do App
        
        """)



# Menu das opções dentro do usuário
def menu_user():
    print("""

        Escolha uma opção:

        [1] - Criar Conta Corrente
        
        [2] - Acessar Conta Corrente

        [3] - Voltar
        
        """)



# Menu da conta corrente 
def menu_conta():
        print("""
            [d] Depositar
            [s] Sacar
            [e] Extrato
            [q] Sair

        """)



def animation(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        for i in range(30):
            time.sleep(0.2)
            print(".", end="", flush=True)
        time.sleep(0.2)
        print("\r", end="", flush=True)



# Função para limpar a tela após a execução de alguns comandos
def limpar_tela():
    os.system("cls") or None



# Função formatação do CPF
def remover_formatacao_cpf(cpf):

    # Remove traços e pontos do CPF
    return cpf.replace(".", "").replace("-", "")



# Function that validates CPF
def validar_cpf():
    while True:
        cpf_to_validate = input("Digite seu CPF: ")

        # Remove dots and dashes
        cpf_user = remover_formatacao_cpf(cpf_to_validate)

        # Verifica se o CPF tem 11 dígitos e não contém letras
        if len(cpf_user) != 11 or not cpf_user.isdigit():
            limpar_tela()
            print("CPF inválido! O CPF deve ter 11 dígitos sem conter letras.")
            continue

        # Verifica se o CPF já está cadastrado
        if cpf_user in users:
            limpar_tela()
            print("CPF já cadastrado!")
            continue
        
        print("CPF válido!")
        return cpf_user



# Function that create and validates Passwords
def validar_senha(): 
        while True:
            password_validate_1 = input("Escolha sua Senha: ")
            print()
            password_validate_2 = input("Confirme sua senha: ")
            print()

            # Valida se a senha confere
            if password_validate_1 == password_validate_2:
                senha = password_validate_2
            else:
                print("A senha não confere, digite novamente.")
                continue

            print("Senha cadastrada com sucesso!!")
            return senha
            

# Funcction that create Users
def criar_user():
    print("Para criar seu usuário siga as instruções a seguir \n")

    cpf = validar_cpf()
    print()
    nome = input("Digite seu nome: ")
    print()
    birth_date = input("Digite sua data de nascimento: ")
    print()

    # Endereço
    nome_rua = input("Digite o nome da sua Rua: ")
    print()
    num_casa = input("Digite o número da sua casa: ")
    print()
    bairro = input("Digite o nome do seu bairro: ")
    print()
    cidade = input("Digite o nome da sua cidade: ")
    print()
    sigla_estado = input("Digite a sigla do seu estado: ").upper()
    print()
    # Senha
    senha = validar_senha()

    # Recebe os dados do endereço e transforma em uma string no formato proposto pelo desafio
    endereco = f"{nome_rua}, {num_casa}, {bairro}, {cidade}/{sigla_estado}"

    # Dicionário que contém os dados do usuário
    user = dict(nome=nome, nascimento=birth_date, cpf=cpf, endereco=endereco, senha = senha, conta_corrente = [])
    global users
    users[cpf] = user

    limpar_tela()

    print("Usuário cadastrado com sucesso!")



def criar_conta(cpf):
    global users
    global AGENCIA
    global num_conta

    print(f"Certo {users[cpf]['nome']}, estamos criando sua nova conta corrente.. \n")
    animation(5)

    # Cria o número da conta
    num_conta += 1

    # Lista onde são armazenados os dados da conta
    ## 0 - Saldo
    ## 1 - Extrato
    ## 2 - Agência
    ## 3 - Número da Conta
    ## 4 - Nome da Conta
    conta_corrente = [0, """""", AGENCIA, num_conta, f"Conta corrente {num_conta}"]

    # Adiciona a conta criada à lista de contas do usuário
    users[cpf]['conta_corrente'].append(conta_corrente)

    # Recupera o índice da nova conta criada (que é o último elemento da lista)
    index = len(users[cpf]['conta_corrente']) - 1

    print(f"Conta {users[cpf]['conta_corrente'][index][4]} criada com sucesso!")



# Função para acessar a conta
def acessar_conta(cpf):
    global users
    num_saques = 0
    total_saques = 0
    

    while True:

        print("********** Lista de Contas **********")

        # Mostra todas as contas do usuário
        for i in range(len(users[cpf]['conta_corrente'])):
            index = i + 1
            print(f"[{index}] - {users[cpf]['conta_corrente'][i][4]}")
        print("[s] - Voltar")
        print()

        # Pede ao usuário que escolha uma conta
        escolha = (input("Escolha uma opção: "))
        limpar_tela()

        if escolha.isdigit() and int(escolha) in range(1, index + 1):
            conta = users[cpf]['conta_corrente'][int(escolha) - 1]  

            # Exibe o nome da conta escolhida e as informações atuais
            print(f"{conta[4]}")
            print()

            menu_conta()
            opcao = input("Escolha a operação que deseja realizar: ")

            if opcao == "d":

                valor = float(input("Digite o valor que deseja depositar: "))

                conta[0] = deposito(valor, conta[0], conta[1])
                conta[1] = gerar_extrato_deposito(valor, conta[1])


            elif opcao == "s":

                valor = float(input("Digite o valor que deseja sacar: "))

                conta[0] = saque(valor, conta[0], conta[1], num_saques, total_saques)
                conta[1] = gerar_extrato_saque(valor, conta[1])
                

            elif opcao == "e":
                visualizar_extrato(conta[0], conta[1], conta[4])

            elif opcao == "q":
                print("Volte sempre!!\n")
                break

            else:
                print("Selecione uma opção válida")

            print()

        elif escolha == "s":
            break



# Realiza login
def login():
    global users  # definir a variável global
    cpf = input("Digite seu CPF (SEM pontos e traços): ")
    senha = input("Digite sua senha: ")

    if cpf in users and users[cpf]["senha"] == senha:
        limpar_tela()
        print(f"Seja Bem Vindo {users[cpf]['nome']}")

        while True:
            menu_user()
            opcao = input("=> ")
            limpar_tela()

            if opcao == "1":
                criar_conta(cpf)
            
            elif opcao == "2":
                acessar_conta(cpf)
            
            elif opcao == "3":
                break


    else:
        print("CPF ou senha inválidos. Ou usuário não encontrado. Tente novamente.")



# Atualiza o extrato de depósito
def gerar_extrato_deposito(valor, extrato):
    extrato += f"R${valor:.2f} C \n"
    return extrato



# Atualiza o extrato de saque
def gerar_extrato_saque(valor, extrato):
    extrato += f"R${valor:.2f} D \n"
    return extrato    



# Função para visualizar extrato
def visualizar_extrato(saldo, extrato, nome_conta):
    print("*************** EXTRATO *****************\n")
    print(f"{nome_conta}")
    print(f"Seu Saldo atual é de R${saldo:.2f}\n")        
    print(f"{extrato}\n")
    print("*****************************************\n")



def deposito(valor, saldo, extrato):

    if valor > 0:
        saldo += valor
        extrato += f"R${valor:.2f} C \n"
        print(f"Valor depositado: R${valor:.2f}")

        return saldo

    else:
        print("Falha, digite um valor válido!")



def saque(valor, saldo, extrato, num_saques, total_saques):

    limite_diario = 500
    limite_saque = 3

    # Condição que o saque será autorizado
    if num_saques < limite_saque and valor <= limite_diario and valor <= saldo and total_saques + valor < limite_diario + 1:
        saldo -= valor
        extrato += f"R${valor:.2f} D \n"
        num_saques += 1
        total_saques += valor
        print(f"valor retirado: R${valor:.2f}")

        return saldo

    else:
        print("Saque não autorizado!")