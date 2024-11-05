import unittest

def obscure_credit_card(card_number):
    if not (12 <= len(card_number) <= 16):
        return "Invalid Credit Card"
    obscured = '*' * (len(card_number) - 4) + card_number[-4:]
    return obscured

class TestObscureCreditCard(unittest.TestCase):
    
    def test_valid_credit_card_12_digits(self):
        self.assertEqual(obscure_credit_card("123456789012"), "********9012")
        
    def test_valid_credit_card_13_digits(self):
        self.assertEqual(obscure_credit_card("1234567890123"), "*********0123")
        
    def test_valid_credit_card_14_digits(self):
        self.assertEqual(obscure_credit_card("12345678901234"), "**********1234")
        
    def test_valid_credit_card_15_digits(self):
        self.assertEqual(obscure_credit_card("123456789012345"), "***********2345")
        
    def test_valid_credit_card_16_digits(self):
        self.assertEqual(obscure_credit_card("1234567890123456"), "************3456")
        
    def test_invalid_credit_card_too_short(self):
        self.assertEqual(obscure_credit_card("12345"), "Invalid Credit Card")
        
    def test_invalid_credit_card_too_long(self):
        self.assertEqual(obscure_credit_card("12345678901234567"), "Invalid Credit Card")
        
    def test_invalid_credit_card_empty(self):
        self.assertEqual(obscure_credit_card(""), "Invalid Credit Card")

if __name__ == "__main__":
    unittest.main()
