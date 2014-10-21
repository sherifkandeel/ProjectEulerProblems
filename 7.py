__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime
import codecs


class problem:
    def __init__(self):
        self.primes = []
        self.load_primes()
        pass

    def load_primes(self):
        with codecs.open('primes_100000.txt') as f:
            for line in f:
                self.primes.append(int(line))
        pass

    def nth_prime(self, n):
        return self.primes[n-1]


if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    print prob.nth_prime(10001)
    end = datetime.now()
    print "--- %d milli seconds ---" % ((end.microsecond-start.microsecond)/1000)



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass

    def test_nth_prime(self):
        self.assertEqual(self.prob.nth_prime(6), 13)
        self.assertEqual(self.prob.nth_prime(1), 2)
        self.assertEqual(self.prob.nth_prime(8), 19)






