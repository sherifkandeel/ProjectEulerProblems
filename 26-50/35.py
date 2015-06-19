__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime
import codecs


class problem:
    def __init__(self):
        self.primes = set()
        self.load_primes()
        pass

    def load_primes(self):
        with codecs.open('primes1m.txt') as f:
            for line in f:
                self.primes.add(int(line))
        print len(self.primes)
        pass

    def is_prime(self,n):
        if self.primes.__contains__(n):
            return True
        return False

    def get_rotations(self,n):
        strn = str(n)
        if len(strn) <2: return [n]
        rotations = []
        for i in range(0,len(strn)):
            div = 10**i
            rm = n % div
            s = n /div
            rotations.append(int(str(rm)+str(s)))
        return rotations

    def is_circularprime(self,n):
        for i in self.get_rotations(n):
            if not self.is_prime(i):
                return False
        return True

    def solve(self):
        count = 1 #counting the only even prime, 2
        for i in range(1,1000001,2):
           if self.is_circularprime(i):
               count+=1

        print count

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

    def test_is_prime(self):
        self.assertTrue(self.prob.is_prime(2))
        self.assertTrue(self.prob.is_prime(5))
        self.assertTrue(self.prob.is_prime(13))
        self.assertFalse(self.prob.is_prime(22))

    def test_rotations(self):
        self.assertEqual(self.prob.get_rotations(179),[179,917,791])


    def test_is_circularprime(self):
        self.assertTrue(self.prob.is_circularprime(197))
        self.assertFalse(self.prob.is_circularprime(18))
