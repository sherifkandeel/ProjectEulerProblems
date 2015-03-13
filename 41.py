__author__ = 'Sherif'
import itertools
from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        pass


    def isPrime(self, n):
        def isSpsp(n, a):
            d, s = n - 1, 0
            while d % 2 == 0:
                d /= 2
                s += 1
            t = pow(a, d, n)
            if t == 1: return True
            while s > 0:
                if t == n - 1: return True
                t = (t * t) % n
                s -= 1
            return False

        for p in [2, 7, 61]:
            if n % p == 0: return n == p
            if not isSpsp(n, p): return False
        return True

    def solve(self):
        largest_prime = 0
        l = "123456789"
        for i in range(1, 9):
            perms = itertools.permutations(l)
            for p in perms:
                integer = self.get_int(p)
                if self.isPrime(integer):
                    if integer > largest_prime:
                        largest_prime = integer
            if largest_prime == 0:
                l = l.strip(l[len(l) - 1])
            else:
                break
        print "largest prime: %d" % largest_prime


    def get_int(self, tup):
        str = ''.join(tup)
        return int(str)


if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    prob.solve()
    end = datetime.now()
    print "--- %s  ---" % (str(end - start))


class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()

    pass





