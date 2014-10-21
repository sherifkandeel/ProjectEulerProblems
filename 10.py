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
        with codecs.open('primes1m.txt') as f:
            for line in f:
                self.primes.append(int(line))
        pass

    def sum_of_primes(self, max):
        sum =0
        for i in range (0, len(self.primes)):
            if self.primes[i] < max:
                sum += self.primes[i]
            else:
                break
        return sum


if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    print prob.sum_of_primes(2000000)
    end = datetime.now()
    print "--- %d milli seconds ---" % ((end.microsecond-start.microsecond)/1000)



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass

    def test_sum_of_primes(self):
        self.assertEqual(self.prob.sum_of_primes(10), 17)





