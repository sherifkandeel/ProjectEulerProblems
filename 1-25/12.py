__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime
import codecs
from sets import Set


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

    def get_prime_factors_iterative(self, n):
        prime_divisors = {}
        i = 0
        while i < len(self.primes):
            if n == 1: break
            if n % self.primes[i] == 0:
                if prime_divisors.has_key(self.primes[i]):
                    prime_divisors[self.primes[i]] += 1
                else:
                    prime_divisors[self.primes[i]] = 1
                n = n / self.primes[i]
            else:
                i += 1
        return prime_divisors

    def get_divisors_count(self, prime_divisors):
        divisors_count = 1
        for k in prime_divisors:
            divisors_count *= (prime_divisors[k] + 1)
        return divisors_count

    def find_triangle_number(self, max):
        i =  1
        adder = 2
        while i >= 1:
            self.set = Set()
            length = self.get_divisors_count(prob.get_prime_factors_iterative(i))
            print "Number:%d Divisors:%d " %(i, length)
            if length > max:
                return i
            i = i + adder
            adder += 1




if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    print prob.find_triangle_number((500))
    end = datetime.now()
    print "--- %d milli seconds ---" % ((end.microsecond-start.microsecond)/1000)



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass




# Essentially it boils down to if your number n is:
# n = a^x * b^y * c^z
# (where a, b, and c are n's prime divisors and x, y, and z are the number of times that divisor is repeated) then the total count for all of the divisors is:
# (x + 1) * (y + 1) * (z + 1).
#
# http://stackoverflow.com/questions/110344/algorithm-to-calculate-the-number-of-divisors-of-a-given-number
