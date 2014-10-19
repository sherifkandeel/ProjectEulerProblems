__author__ = 'Sherif'
from unittest import TestCase
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
        print len(self.primes)
        pass

    def largest_prime(self, number):
        largest_prime = 0
        for i in range(0, len(self.primes)):
            if number % self.primes[i] == 0:
                largest_prime = self.primes[i]
        return largest_prime



if __name__ == "__main__":
    prob = problem()
    print prob.largest_prime(600851475143)



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass

    def test_largest_prime(self):
        self.assertEqual(self.prob.largest_prime(13195), 29)
    pass


