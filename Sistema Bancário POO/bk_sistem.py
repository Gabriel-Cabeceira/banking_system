from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

# List of users
users = []
accounts = []

# Class that represents the simple User
class User:
    def __init__(self, address, email, password):
        self.accounts = []
        self.address = address
        self.email = email
        self.password = password

    def perform_transaction(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        self.accounts.append(account)

    @classmethod
    def create_user(cls, address, email, password, **kwargs):
        if "name" in kwargs and "birthday" in kwargs and "cpf" in kwargs:
            return Individual(address, email, password, **kwargs)
        elif "name" in kwargs and "cnpj" in kwargs:
            return Legal_Entity(address, email, password, **kwargs)
        else:
            raise ValueError("Invalid user information")

    @staticmethod
    def authenticate(email, password):
        for user in users:
            if user.email == email and user.password == password:
                return user
        return None


# Subclass of User that represents an individual/Personal user
class Individual(User):
    def __init__(self, address, email, password, name, birthday, cpf):
        super().__init__(address, email, password)

        self.name = name
        self.birthday = birthday
        self.cpf = cpf

    def __str__(self):
        return f"Pessoa Física: {self.address}, {self.email}, {self.password}, {self.name}, {self.birthday}, {self.cpf}"


# Subclass of User that represents an enterprise user
class Legal_Entity(User):
    def __init__(self, address, email, password, name, cnpj):
        super().__init__(address, email, password)

        self.name = name
        self.cnpj = cnpj

    def __str__(self):
        return f"Pessoa Jurídica: {self.address}, {self.email}, {self.password}, {self.name}, {self.cnpj}"


# Class that represents a simple account
class account:
    def __init__(self, id_account, user):
        self._balance = 0
        self._agency = "0001"
        self._historic = Historic()
        self._id_account = id_account
        self._user = user

    @classmethod
    def new_account(cls, user, id_account, type_account):
        if type_account == "1":
            return current_account(id_account, user, type_account)
        else:
            print("Tipo inválido, selecione um tipo válido")
            return None
    
    @property
    def balance(self):
        return self._balance
    
    @property
    def id_account(self):
        return self._id_account
    
    @property
    def agency(self):
        return self._agency
    
    @property
    def user(self):
        return self._user
    
    @property
    def historic(self):
        return self._historic
    
    def withdrawal(self, value):
        balance = self._balance
        value_exceeded = value > balance

        if value_exceeded:
            print("\n Falha na operação, você não tem saldo suficiente.")

        elif value > 0:
            self._balance -= value
            print("\n Saque realizado com sucesso!")
            return True
        
        else:
            print("Falha! Valor inválido.")
            return False
        
    def deposit(self, value):
        if value > 0:
            self._balance += value
            print("Depósito realizado com sucesso!")

        else:
            print("Falha na operação! Valor inválido")
            return False
        
        return True

# Subclass of Account that represents the current account type
class current_account(account):
    def __init__(self, id_account, user, type_account, limit_value=500, limit_withdrawal=3):
        super().__init__(id_account, user)
        self._limit_value = limit_value
        self._limit_withdrawal = limit_withdrawal
        self._type = type_account

        def withdrawal(self, value):
            withdrawal_quantity = len([transaction for transaction in self.historic.transactions if transaction["type"] == Withdrawal.__name__])


            limit_exceeded = value > self._limit_value
            limit_withdrawal_exceeded = withdrawal_quantity >= self._limit_withdrawal
        
            if limit_exceeded:
                print("Falha! o valor do Saque excede o limite permitido para sua conta.")

            elif limit_withdrawal_exceeded:
                print("Falha! Número máximo de saques excedido.")

            else:
                return super().withdrawal(value)
            
            return False
        
        def __str__(self):
            return f"""
                    Agência:\t{self.agency}
                    C/C:\t\t{self.id_account}
                    Titular:\t{self.user.name}
                    """

class Historic:
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions
        
    def add_transaction(self, transaction):
        self._transactions.append(
            {
                "type": transaction.__class__.__name__,
                "value": transaction.value,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }
        )

class Transaction(ABC):
    @property
    @abstractproperty
    def value(self):
        pass

    @abstractclassmethod
    def register(self, account):
        pass

class Withdrawal(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    
    def register(self, account):
        transaction_success = account.withdrawal(self.value)

        if transaction_success:
            account.historic.add_transaction(self)

class Deposit(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    
    def register(self, account):
        transaction_success = account.deposit(self.value)

        if transaction_success:
            account.historic.add_transaction(self)