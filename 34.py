__author__ = 'sherif'
from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        self.fact_dict = {}
        self.fact_dict[1] = 1
        self.fact_dict[2] = 2
        pass

    def factorial(self, n):
        if n == 1 or n == 0: return 1
        if self.fact_dict.has_key(n):
            return self.fact_dict[n]
        self.fact_dict[n] = n * self.factorial(n - 1)
        return self.fact_dict[n]

    def is_curious(self, n):
        if n == 1 or n == 2: return False
        total = 0
        for d in str(n):
            total += self.factorial(int(d))
            if total > n:
                return False
        if total == n:
            return True
        return False

    def solve(self):
        total =0
        for i in range(1, 9999999):
            if self.is_curious(i):
                total+=i
                print i
        print total


if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    prob.solve()
    end = datetime.now()
    print "--- %s  ---" % (str(end - start))


class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()

    pass

    def test_factorial(self):
        self.assertEqual(self.prob.factorial(3), 6)
        self.assertEqual(self.prob.factorial(5), 120)
        print self.prob.fact_dict

    def test_is_curious(self):
        self.assertTrue(self.prob.is_curious(145))
        self.assertFalse(self.prob.is_curious(1))
        self.assertFalse(self.prob.is_curious(123))

