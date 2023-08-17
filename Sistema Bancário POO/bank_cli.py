from bk_sistem import *
import os

def select_account(user):
    print("\n===== Suas Contas =====")
    for i, account in enumerate(user.accounts, start=1):
        print(f"{i}. Agência: {account.agency} | Conta: {account.id_account}")
    print("========================")

    choice = input(": ")
    if not choice.isdigit():
        print("Escolha inválida.")
        return None

    account_index = int(choice) - 1
    if 0 <= account_index < len(user.accounts):
        return user.accounts[account_index]
    else:
        print("Escolha inválida.")
        return None

def deposit_user(user):
    value = float(input("Digite o valor que deseja depositar: "))
    transaction = Deposit(value)
    account = select_account(user)
    
    if not account:
        return
    
    user.perform_transaction(account, transaction)

def withdraw_user(user):
    value = float(input("Informe o valor que deseja sacar: "))
    transaction = Withdrawal(value)
    account = select_account(user)
    
    if not account:
        return
    
    user.perform_transaction(account, transaction)

def account_statement_user(user):
    account = select_account(user)
    
    if not account:
        return
    
    print("\n================ EXTRATO ================")
    transactions = account.historic.transactions

    statement = ""
    if not transactions:
        statement = "Nenhuma transação foi realizada."
    else:
        for transaction in transactions:
            statement += f"\n{transaction['type']}:\n\t$ {transaction['value']:.2f} - {transaction['date']}"

    print(statement)
    print(f"\nSaldo:\n\t$ {account.balance:.2f}")
    print("==========================================")

def new_account_user(user):
    account_id = len(accounts) + 1
    account_type = input("Escolha o tipo de conta (1 para conta corrente): ")
    account_user = account.new_account(user, account_id, type_account=account_type)

    if not account_user:
        return

    user.add_account(account_user)
    accounts.append(account_user)
    print("\n=== Nova conta criada com sucesso! ===")

def list_accounts_user(user):
    print("\n===== Lista de Contas =====")
    for account in user.accounts:
        print(f"Agencia: {account.agency} | Conta: {account.id_account}")
    print("========================")

def navegation_account(user):
    while True:
        account_menu()
        option = input("=> ")
        clear_screen()

        if option == "d":
            deposit_user(user)

        elif option == "s":
            withdraw_user(user)

        elif option == "e":
            account_statement_user(user)
        
        elif option == "nc":
            new_account_user(user)

        elif option == "lc":
            list_accounts_user(user)

        elif option == "q":
            print(f"Até logo {user.name}! \n Volte sempre")
            break

        else:
            print("Opção inválida. Tente novamente. \n")

def initial_menu():
    print("""

    ================ Banco GC ================

        Escolha uma opção:

        [1] - Fazer Login
        
        [2] - Criar novo Usuário

        [3] - Sair do App
        
        """)
    
def account_menu():
    print("""
            ================ MENU ================
            [d] Depositar
            [s] Sacar
            [e] Extrato
            [nc] Nova Conta
            [lc] Listar Contas
            [q] Sair

        """)
            
def clear_screen():
    os.system("cls") or None

def create_user():
    endereco = input("Digite um endereço: ")
    email = input("Digite um email: ")
    senha = input("Escolha uma senha: ")
    nome = input("Informe seu nome: ")
    nascimento = input("Informe sua data de Nascimento: ")
    cpf = input("Informe seu CPF: ")

    new_user = User.create_user(endereco, email, senha, name=nome, birthday=nascimento, cpf=cpf)
    users.append(new_user)

def login():
        
    email = input("Digite seu email: ")
    password = input("Digite sua Senha: ")
    authenticated_user = User.authenticate(email, password)

    while not authenticated_user:
        print("Usuário ou senha inválidos\n")
        email = input("Digite seu email: ")
        password = input("Digite sua Senha: ")
        authenticated_user = User.authenticate(email, password)

    navegation_account(authenticated_user)
           

while True:

    initial_menu()

    opcao = input("=> ")
    clear_screen()

    if opcao == "1":
        login()

    elif opcao == "2":
        create_user()

    elif opcao == "3":
        print("Volte sempre!!\n")
        break

    else:
        print("Digite uma opção válida: ")


