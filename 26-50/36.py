__author__ = 'sherif'
from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        pass

    def is_palindrome(self, n):
        ln = len(n)
        for i in range(0,ln/2):
            if n[i] != n[ln-1-i]:
                return False
        return True

    def convert_to_binary_str(self,n):
        b = str(bin(n))
        return b.replace("0b","")

    def is_double_base_palindrome(self,n):
        if self.is_palindrome(str(n)) and self.is_palindrome(self.convert_to_binary_str(n)):
            return True
        return False

    def solve(self):
        sum = 0
        for i in range(1,1000001):
            if self.is_double_base_palindrome(i):
                sum+=i
                print "%d --> %s"%(i,self.convert_to_binary_str(i))

        print sum


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

    def test_is_palindrome(self):
        self.assertTrue(self.prob.is_palindrome("10001"))
        self.assertTrue(self.prob.is_palindrome("1001"))
        self.assertTrue(self.prob.is_palindrome("1"))
        self.assertFalse(self.prob.is_palindrome("231"))
