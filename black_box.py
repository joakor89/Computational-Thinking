import unittest

def sum(num_1, num_2):
    return num_1 + num_2

class BlackBoxTest(unittest.TestCase):

    def add_sum_two_positive(self):
        num_1 = 10
        num_2 = 5 

        outcome = sum(num_1, num_2)

        self.assertEqual(outcome, 15)

    def add_sum_two_negative(self):
        num_1 = -10
        num_2 = -7

        outcome = sum(num_1, num_2)

        self.assertEqual(outcome, -17)


if __name__ == '__main__':
    unittest.main()

    



    