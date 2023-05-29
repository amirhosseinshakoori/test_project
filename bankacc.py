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