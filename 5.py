__author__ = 'Sherif'
from unittest import TestCase


class problem:
    def is_divisible(self, number, divisive):
        if number % divisive == 0:
            return True
        return False

    def get_smallest_multiple(self, min, max):
        divisable = False
        number =0
        while divisable == False:
            number += 1
            for i in range(min, max):
                if number % i != 0:
                    divisable = False
                    break
                divisable=True

        return number








if __name__ == "__main__":
    prob = problem()
    print prob.get_smallest_multiple(11,21)


#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#find divisors
#11 12 13 14 15 16 17 18 19 20
#another solution is to calculate the prime factorization for that number
# 20 = 2^2 * 5
# 19 = 19
# 18 = 2 * 3^2
# 17 = 17
# 16 = 2^4
# 15 = 3 * 5
# 14 = 2 * 7
# 13 = 13
# 11 = 11
#
# All others are included in the previous numbers.
#
# ANSWER: 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232 792 560

class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass

    def test_is_divisible(self):
        self.assertTrue(self.prob.is_divisible(10,5))
        self.assertTrue(self.prob.is_divisible(33,3))
        self.assertTrue(self.prob.is_divisible(12,6))
        self.assertFalse(self.prob.is_divisible(13,5))

    def test_smallest_multiple(self):
        self.assertEqual(self.prob.get_smallest_multiple(1,11), 2520)


