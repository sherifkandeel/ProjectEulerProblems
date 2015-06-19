__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime
from itertools import permutations

class problem:
    def __init__(self):
        pass


    def get_permutations_pandigital(self, s):
        perms = [''.join(p) for p in permutations(s)]
        return perms

#    def get_substrings(self, s):
#        arr = []
#        for i in range(1,len(s)-2):
#            arr.append(s[i:i+3])
#        return arr
#
#    def has_the_property(self, arr):
#        primes = [2,3,5,7,11,13,17]
#        for i in range(0,len(arr)):
#            if int(arr[i]) % primes[i] !=0:
#                return False
#        return True

    def has_the_prober(self, s):
        primes = [2,3,5,7,11,13,17]
        for i in range(1,len(s)-2):
            portion = s[i:i+3]
            if int(portion) % primes[i-1] !=0:
                return False
        return True

    def solve(self):
        total = 0
        perms = self.get_permutations_pandigital("0123456789")
        for perm in perms:
#            if self.has_the_property(self.get_substrings(perm)):
            if self.has_the_prober(perm):
                total+=int(perm)
        return total



if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    print prob.solve()
    end = datetime.now()
    print "--- %s  ---" % (str(end-start))



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass




#of course people started with multiples of 17 then took those and extracted the ones with multiples of 13 then multiples of 11....etc 
