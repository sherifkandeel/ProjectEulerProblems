from sets import Set

__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        pass

    def solve(self, a, b):
        sequence = Set()
        for i in range(2, a+1):
            for j in range(2, b+1):
                sequence.add(i**j)
        return len(sequence)





if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    print prob.solve(100,100)
    end = datetime.now()
    print "--- %s  ---" % (str(end - start))


class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()

    pass

    def test_solve(self):
        self.assertEqual(self.prob.solve(5,5),15)




