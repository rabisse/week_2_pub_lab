import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John", 20, 100, 1)

    def test_customer_name(self):
        self.assertEqual("John", self.customer.name)

    def test_customer_wallet(self):
        self.assertEqual(100, self.customer.wallet)

    def test_increase_drunkenness(self):
        drink = Drink("beer", 5, 1)
        self.customer.increase_drunkenness(drink)
        self.assertEqual(2, self.customer.drunkenness)

    def test_decrease_drunkenness(self):
        food = Food("Chips", 4, 1)
        self.customer.decrease_drunkenness(food)
        self.assertEqual(0, self.customer.drunkenness)

    def test_already_sober(self):
        food = Food("Burger", 5, 3)
        self.customer.decrease_drunkenness(food)
        self.assertEqual(0, self.customer.drunkenness)

    def test_increase_wallet(self):
        money = 10
        self.customer.increase_wallet(money)
        self.assertEqual(110, self.customer.wallet)

    def test_decrease_wallet(self):
        money = 10
        self.customer.decrease_wallet(money)
        self.assertEqual(90, self.customer.wallet)

