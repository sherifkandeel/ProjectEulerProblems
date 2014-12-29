__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        pass

    def sum(self, size):
        sum = 0
        multi = 2
        start = 1
        for i in range(1, size * 2):
            sum += start
            start = start + multi
            if i % 4 == 0:
                multi += 2
        return sum


if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    print prob.sum(1001)
    end = datetime.now()
    print "--- %s  ---" % (str(end - start))


class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()

    pass

    def test_sum(self):
        self.assertEqual(self.prob.sum(5), 101)



# can be done using euler equations as well but me

