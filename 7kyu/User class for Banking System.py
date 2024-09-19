class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    
    def withdraw(self, n):
        if self.balance < n:
            raise ValueError(f"{self.name} has not enough money to withdraw.")
        
        self.balance -= n
        return f"{self.name} has {self.balance}."
    
    def check(self, other, n):
        if other.balance < n:
            raise ValueError(f"{other.name} has not enough money to transfer money to {self.name}.")
        elif not other.checking_account:
            raise ValueError(f"{other.name}'s balance account is closed.")
        
        self.balance += n
        other.balance -= n
        
        return f"{self.name} has {self.balance} and {other.name} has {other.balance}."
        
    
    def add_cash(self, n):
        self.balance += n
        return f"{self.name} has {self.balance}."