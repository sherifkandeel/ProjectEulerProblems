__author__ = 'Sherif'
from unittest import TestCase


class problem:
    def next_fibonacci(self, prev1, prev2):
        return prev1+prev2

    def is_even(self, number):
        if number %2 == 0:
            return True
        return False

    def sum(self, max):
        prev1= 1
        prev2= 2
        current = 0
        sum = 2
        while current <= max:
            current = self.next_fibonacci(prev1, prev2)
            prev1 = prev2
            prev2 = current
            if self.is_even(current):
                sum+= current
        return sum


def run():
    prob  = problem()
    print prob.sum(4000000)
    pass

if __name__ == "__main__":
    run()
    pass


class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
        pass

    def test_next_fibonacci(self):
        self.assertEqual(self.prob.next_fibonacci(1, 2), 3)
        self.assertEqual(self.prob.next_fibonacci(2, 3), 5)
        pass

    def test_is_even(self):
        self.assertTrue(self.prob.is_even(2))
        self.assertFalse(self.prob.is_even(3))
        self.assertFalse(self.prob.is_even(3998889))
        pass

    def test_sum(self):
        self.assertEqual(self.prob.sum(10), 10)
        self.assertEqual(self.prob.sum(35), 44)
        self.assertEqual(self.prob.sum(4000000), 4613732)
        pass
