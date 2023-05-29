import random
import uuid
import hashlib
import getpass
import json
import datetime
import re
from typing import List, Tuple

MIN_BALANCE = 10_000 # Minimum balance of 10_000T
FEE = 0.005 # 0.005T fee per transaction   

class BankAccount:
    
    accounts = {}   # Stores all accounts 
    
    def __init__(self,name: str, balance=0, password="", card=None):
        """
        Initialize a new BankAccount object.

        Args:
            name (str): The name of the account holder.
            balance (float, optional): The initial account balance. Defaults to 0.
            password (str, optional): The password for the account. Defaults to ''.
        """
        # 
        self.name = name 
        self.balance = balance   
        self.account_number = str(uuid.uuid4())[:8] 
        self.password = self.set_password()    
        # self.card = Card().generate_card(self.account_number)
        self.transaction_history = []
        BankAccount.accounts[self.card.card_number] = self

    @property
    def balance(self) -> float:
        """Get the current account balance."""
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        """
        Set the current account balance.

        Args:
            value (float): The new account balance.
        """
        self._balance = value


    def set_password(self, password: str) -> None:
        """
        Set the password for the account.

        Args:
            password (str): The new password for the account.
        """
        password = getpass.getpass()
        password2 = getpass.getpass()
        if password == password2:  
            password = password.encode()     
            hash_object = hashlib.sha256(password)
            hashed_password = hash_object.hexdigest()
        return hashed_password
    
    def deposit(self, amount: float) -> None:
        """
        Add funds to the account balance.

        Args:
            amount (float): The amount to deposit.
        """
        self.balance += amount
        self.transaction_history.append(("Deposit", amount))

    def withdraw(self, amount: float) -> None:
        """
        Subtract funds from the account balance.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the specified amount is greater than the account balance.
        """
        if self.balance - amount < MIN_BALANCE:
             print("Insufficient funds")
        else:
            self.balance -= amount + FEE
            if amount > self.balance:
                return False
            else:
             self.balance -= amount
             self.transaction_history.append(("Withdrawal", amount))
             return True


    def check_balance(func):
    
        def wrapper(self, *args, **kwargs):  
      
        # Check if account has enough balance
            if self.balance < MIN_BALANCE:
                print("Insufficient funds") 
            return
            
       # Call original function   
            return func(self, *args, **kwargs)
        
        return wrapper

    def transfer(self, amount: float, recipient: 'BankAccount', password: str) -> None:
        """
        Transfer funds to another account.

        Args:
            amount (float): The amount to transfer.
            recipient (BankAccount): The account to transfer funds to.
            password (str): The password for the sender's account.

        Raises:
            ValueError: If the specified amount is greater than the 
            account balance or if the password is incorrect.
        """
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        if password != self.password:
            raise ValueError("Incorrect password")
        self.balance -= amount
        self.balance -= self.calculate_fees(amount)
        self.transaction_history.append(('Transfer', amount, recipient.account_number))
        recipient.deposit(amount)

    def get_transaction_history(self) -> List[Tuple[str, float]]:
        """
        Get the transaction history for the account.

        Returns:
            List[Tuple[str, float]]: A list of tuples representing 
            the transaction history, where each tuple contains the type
            of transaction ('Deposit', 'Withdrawal', or 'Transfer') 
            and the amount involved.
        """
        return self.transaction_history
    

    def get_balance(self):
         return self.balance
    

    def apply_fee(self, amount):
         self.balance -= amount


    def validate_password(self, password):
        password = password.encode()        
        hash_object = hashlib.sha256(password) 
        hashed_password = hash_object.hexdigest()        
        return hashed_password == self.password
    
    def save_accounts(self):
        """Save all accounts to a JSON file."""
        with open('accounts.json', 'w') as f:
            json.dump(BankAccount.accounts, f)


    def load_accounts(self):
        """Load account data from a JSON file."""
        with open('accounts.json') as f:
            data = json.load(f)
        BankAccount.accounts = data