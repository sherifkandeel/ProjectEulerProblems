__author__ = 'Sherif'
from unittest import TestCase
import time
from datetime import datetime


class problem:
    def sum_of_squares(self, max):
        sum =0
        for i in range(1, max+1):
            sum += i*i
        return sum

    def square_of_sums(self,max):
        sum =0
        for i in range(1, max+1):
            sum += i
        return sum*sum

    def sum_square_diff(self,max):
        return self.square_of_sums(max) - self.sum_of_squares(max)




if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    print prob.sum_square_diff(100)
    end = datetime.now()
    print "--- %d milli seconds ---" % (end.microsecond-start.microsecond)


class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass

    def test_sum_of_squares(self):
        self.assertEqual(self.prob.sum_of_squares(10),385)

    def test_square_of_sums(self):
        self.assertEqual(self.prob.square_of_sums(10), 3025)

    def test_sum_square_diff(self):
        self.assertEqual(self.prob.sum_square_diff(10), 2640)



# (1+2+...+99+100)^2 = (101 * 50)^2 = 25 502 500
#
# 1^2 + 2^2 + 3^2 + ... + 99^2 + 100^2 = 338 350
#
# Squares are also the sum of odd numbers, so this is also equal to:
#
# = 100*1 + 99*3 + 98*5 +...+ 2*197 + 1*199
#
