__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime
import math
import codecs

class problem:
    def __init__(self):
        self.primes= []
        self.primes_set = set()
        self.load_primes()
        pass

#    def generate_squares(self, max):
#        adder = 1
#        counter = 1
#        for i in range(1,max):
#            adder +=2
#            counter+=adder
#            number = counter
#            print number*2

    def load_primes(self):
        with codecs.open('/home/sherifkandeel/work/ProjectEulerProblems/primes1m.txt') as f:
            for line in f:
                self.primes.append(int(line))
                self.primes_set.add(int(line))
        print len(self.primes)
        pass

    def is_prime(self,n):
        if self.primes_set.__contains__(n):
            return True
        return False

    def is_square(self, number):
        x = math.sqrt(number)
        return x == int(x)

    def is_following_conjecture(self,number):
        if self.is_prime(number):
            return True
        for p in self.primes:
            if p>= number:
                break
            remain = (number-p)/2
            if self.is_square(remain):
                return True
        return False

    def solve(self):
        counter = 27
        while True:
            if not self.is_following_conjecture(counter):
                print "holy moly, we found it... it's %d"% counter
                break
            counter+=2







if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    prob.solve()
    end = datetime.now()
    print "--- %s  ---" % (str(end-start))



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass





