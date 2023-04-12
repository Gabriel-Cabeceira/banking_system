# funções externas
import os
from funcoes import *


def main():

    while True:
        initial_menu()

        opcao = input("=> ")
        limpar_tela()

        if opcao == "1":
            login()

        elif opcao == "2":
            criar_user()

        elif opcao == "3":
            print("Volte sempre!!\n")
            break

        else:
            print("Digite uma opção válida: ")



if __name__ == "__main__":
    main()
