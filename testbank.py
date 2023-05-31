import unittest
import datetime
from bankacc import BankAccount
FEE = 0.005

class TestBankAccount(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.account = BankAccount("JohnDoe", 500)


    def test_generate_account_number(self):
        number = BankAccount.generate_account_number()
        self.assertTrue(len(number) == 16)
    
    def test_balance(self):
        balance = self.account.get_balance()
        self.assertEqual(balance, 500)
        self.account.deposit(100)   
        balance = self.account.get_balance()
        self.assertEqual(balance, 600)   
        self.account.withdraw(50)            
        balance = self.account.get_balance() 
        self.assertEqual(balance, 550)   

    def test_set_password(self):
        password = self.account.set_password("password", "password")          
        self.assertFalse(self.account.validate_password("wrong password"))      
        self.assertTrue(self.account.validate_password(password))
    
    def test_deposit(self):
        self.account.deposit(100)   
        self.account.get_balance()        
        self.assertEqual(600)  
    
    def test_withdraw(self): 
        self.account.withdraw(100)     
        self.account.deposit(50)        
        self.account.withdraw(25)
        balance = self.account.get_balance()
        self.assertEqual(balance, 425)
        
    def test_transfer(self):
        amount = 100
        other_account = BankAccount("Jane Doe", 600)
        self.account.transfer(amount, other_account)       
        recipient = BankAccount("Jane Doe")   
        self.account.transfer(50, recipient, self.account.password)
        sender_balance = self.account.get_balance()          
        recipient_balance = recipient.get_balance() 
        self.assertEqual(sender_balance, 350)  
        self.assertEqual(recipient_balance, 50) 

if __name__ == '__main__':
    unittest.main() 