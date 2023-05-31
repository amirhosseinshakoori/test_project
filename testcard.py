import unittest
import datetime
from bankacc import Card

class TestCard(unittest.TestCase):
    
    
    def test_generate_number(self):
        number = Card.generate_number()
        self.assertEqual(len(number), 16) 
        self.assertRegex(number, "^610433\d{10}$") 
        
    def test_calculate_check_digit(self): 
        check_digit = Card.calculate_check_digit("610433000000000000")
        self.assertEqual(check_digit, 3)
        
    def test_generate_cvv(self):   
        cvv = Card.generate_cvv()      
        self.assertGreaterEqual(cvv, 100)   
        self.assertLessEqual(cvv, 999) 
        
    def test_generate_exp_date(self):    
        exp_date = Card.generate_exp_date()  
        self.assertGreaterEqual(exp_date, datetime.date.today())   
        self.assertLessEqual((exp_date - datetime.date.today()).days, 1825)




if __name__ == '__main__':
    unittest.main()