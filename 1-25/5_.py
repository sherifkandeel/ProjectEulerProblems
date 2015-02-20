__author__ = 'Sherif'
from unittest import TestCase
import time
import codecs


class problem:
    def __init__(self):
        self.primes = []
        # self.prime_factors = []
        self.iterator = 0
        self.divisors = []

        self.load_primes()
        pass

    def load_primes(self):
        with codecs.open('primes_100000.txt') as f:
            for line in f:
                self.primes.append(int(line))
        print len(self.primes)
        pass

    def get_next_prime(self):
        next = self.primes[self.iterator]
        self.iterator += 1
        return next


    def get_prime_factors(self, n, prime):
        if n == 1: return
        if n % prime == 0:
            self.divisors.append(prime)
            self.get_prime_factors(n/prime,prime)
        else:
            self.get_prime_factors(n, self.get_next_prime())
        return self.divisors

    def get_smallest_multiple(self, min, max):
        for i in range(min, max):
            self.iterator = 0
            self.get_prime_factors(i, self.get_next_prime())

        print self.divisors
        smallest_multiple = 1
        for i in self.divisors:
            smallest_multiple *= i

        return smallest_multiple


if __name__ == "__main__":
    start_time = time.time()
    prob = problem()
    print("--- %s seconds ---" % time.time() - start_time)



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass

    def test_get_next_prime(self):
        self.assertEqual(self.prob.get_next_prime(), 2)
        self.assertEqual(self.prob.get_next_prime(), 3)
        self.assertEqual(self.prob.get_next_prime(), 5)
        self.assertEqual(self.prob.get_next_prime(), 7)
        self.assertEqual(self.prob.get_next_prime(), 11)

    def test_get_prime_factors(self):
        self.assertEqual(self.prob.get_prime_factors(20, self.prob.get_next_prime()), [2, 2, 5])
        self.prob = problem()
        self.assertEqual(self.prob.get_prime_factors(10, self.prob.get_next_prime()), [2, 5])

    def test_smallest_multiple(self):
        self.assertEqual(self.prob.get_smallest_multiple(1, 11), 2520)

    



