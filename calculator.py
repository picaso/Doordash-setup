import unittest

# Can multiply two numbers
# Can divide two numbers

class CalculatorTest(unittest.TestCase):
    def test_should_add_two_numbes(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2,2), 4, "output should be 4")

    def test_should_be_able_to_add_more_than_two_numbers(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(3,2,6), 11, "output should be 11")

def test_should_find_difference_between_two_numbers(self):
        calculator = Calculator()
        self.assertEqual(calculator.difference(2,2), 0)



class Calculator():
    def add(self, *args):
        sum = 0 
        for arg in args:
            sum = sum + arg
        return sum

    def difference(self, a, b):
        return a - b
