__author__ = 'Sherif'
from unittest import TestCase


class problem:
    def is_palindrome(self, number):
        max = len(number)
        for i in range(0, max):
            if number[i] != number[max-1-i]:
                return False
        return True

    def largest_palindrome_product(self, n):
        number = pow(10, n)
        print number
        largest_palindrome=0
        for i in range(1, number):
            for j in range(1, number):
                prod = i*j
                if self.is_palindrome(str(prod)):
                    if prod>largest_palindrome:
                        largest_palindrome = prod
        return largest_palindrome



if __name__ == "__main__":
    prob = problem()
    print prob.largest_palindrome_product(3)


class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass

    def test_is_palindrome(self):
        self.assertTrue(self.prob.is_palindrome("abccba"))
        self.assertTrue(self.prob.is_palindrome("abcscba"))
        self.assertTrue(self.prob.is_palindrome("a"))
        self.assertFalse(self.prob.is_palindrome("abcssascba"))
        pass

    def test_largest_palindrome_product(self):
        self.assertEqual(self.prob.largest_palindrome_product(2), 9009)
        pass
