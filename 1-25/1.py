__author__ = 'Sherif'
from unittest import TestCase


class problem:
    def determinemultiple(self, number):
        if number != 0 and (number % 3 == 0 or number % 5 == 0):
            return True
        return False
        pass

    def sum(self, max):
        sum = 0
        for i in range(1, max):
            if self.determinemultiple(i):
                sum+= i
        return sum

def run():
    prob = problem()
    print prob.sum(1000)



if __name__ == "__main__":
    run()




class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
        pass

    def test_determinemultiple(self):
        self.assertTrue(self.prob.determinemultiple(3))
        self.assertTrue(self.prob.determinemultiple(5))
        self.assertTrue(self.prob.determinemultiple(15))
        self.assertFalse(self.prob.determinemultiple(1))
        self.assertFalse(self.prob.determinemultiple(0))
        pass

    def test_iterate(self):
        self.assertEqual(self.prob.sum(10), 23)
        self.assertEqual(self.prob.sum(11), 33)
        pass