__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime
import codecs
from sets import Set


class problem:
    def __init__(self):
        self.primes = []
        # self.prime_factors = []
        # self.iterator = 0
        # self.divisors = []
        self.load_primes()
        self.set = Set()
        pass

    def load_primes(self):
        with codecs.open('primes1m.txt') as f:
            for line in f:
                self.primes.append(int(line))
        # print len(self.primes)
        pass

    # def get_next_prime(self):
    #     next = self.primes[self.iterator]
    #     self.iterator += 1
    #     return next


    # def get_prime_factors(self, n, prime):
    #     print "%d %d" %(n, prime)
    #     if n == 1: return
    #     if n % prime == 0:
    #         self.divisors.append(prime)
    #         self.get_prime_factors(n/prime, prime)
    #     else:
    #         self.get_prime_factors(n, self.get_next_prime())
    #     return self.divisors

    # def get_prime_factors_iterative(self, n, prime):
    #     if n ==1: return
    #     for i in range (0, len(self.primes)):
    #         if n % self.primes[i] == 0:
    #             self.divisors.append(self.primes[i])
    #             self.get_prime_factors_iterative(n/prime, prime)
    #     return self.divisors

    def get_prime_factors_iterative(self, n):
        prime_divisors = []
        i = 0
        while i < len(self.primes):
            if n == 1: break
            if n % self.primes[i] == 0:
                prime_divisors.append(self.primes[i])
                n = n/ self.primes[i]
            else:
                i += 1
        return prime_divisors


    def get_non_prime_divisors(self, number):
        prime_divisors = self.get_prime_factors_iterative(number)
        for i in range(0, len(prime_divisors)):
            for j in range(i+1, len(prime_divisors)):
                self.set.add(prime_divisors[i] * prime_divisors[j])
            self.set.add(prime_divisors[i])
        self.set.add(1)
        self.set.add(number)
        return self.set

    def find_triangle_number(self, max):
        i =  1
        adder = 2
        while i >= 1:
            self.set = Set()
            length = len(self.get_non_prime_divisors(i))
            print "Number:%d Divisors:%d " %(i, length)
            if length > max:
                return i
            i = i + adder
            adder += 1








if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    print prob.find_triangle_number(500)
    end = datetime.now()
    print "--- %d milli seconds ---" % ((end.microsecond-start.microsecond)/1000)



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass

    def test_get_non_prime_divisors(self):
        S = Set([1, 2, 4, 7, 14, 28])
        self.assertEqual(self.prob.get_non_prime_divisors(28), S)
        self.assertEqual(self.prob.get_non_prime_divisors(31828023451), S)
        # self.assertEqual(self.prob.get_non_prime_divisors(34072898628), S)

    def test_get_prime_factors_iterative(self):
        self.assertEqual(self.prob.get_prime_factors_iterative(425), [5, 5, 17])
        self.assertEqual(self.prob.get_prime_factors_iterative(31828023451), [5, 5, 17])

    def test_find_triangle_number(self):
        self.assertEqual(self.prob.find_triangle_number(5), 28)





