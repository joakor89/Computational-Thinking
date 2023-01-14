import unittest

def adul(age):
    if age >= 18:
        return True
    else:
        return False



class CrystalBoxTest(unittest.TestCase):
    
    def adult_test(self):
        age = 20

        outcome = adult(age)

        self.assertEqual(outcome, True)

    def underage_test(self):
        age = 15

        outcome = adult(age)

        self.assertEqual(outcome, False)


if __name__ == '__main__':
    unittest.main()
