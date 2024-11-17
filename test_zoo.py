import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_priceC1b1(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "ERROR") # Fault 1 is fixed

    def test_child_ticket_priceC1b2(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50) # Fault 2  is fixed

    def test_child_ticket_priceC1b3(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100) # Fault 3  is fixed

    def test_child_ticket_priceC1b4(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150) # Fault 4  is fixed

    def test_child_ticket_priceC1b5(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100) 

    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()
