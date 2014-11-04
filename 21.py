__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime
import codecs
import copy
from sets import Set


class problem:
    def __init__(self):

        pass

    def get_divisors_brute_force(self, number):
        divisors=[]
        for i in range(1, int(number*0.5)+1):
            if number % i == 0:
                divisors.append(i)
        return divisors

    def sum_of_divisors(self, number):
        divisors= 0
        for i in range(1, int(number*0.5)+1):
            if number % i == 0:
                divisors += i
        return divisors

    def amicale_numbers(self):
        numbers_sum = {}
        for i in range(1,10001):
            numbers_sum[i] = self.sum_of_divisors(i)

        amicales = Set()
        for numb in numbers_sum:
            val = numbers_sum[numb]
            if val>0 and val<10000 and val !=numb and numbers_sum[val] == numb:
                amicales.add(numb)
                amicales.add(val)

        print sum(amicales)


if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    prob.amicale_numbers()

    end = datetime.now()
    print "--- %s  ---" % (str(end-start))



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass


    # def test_get_divisors(self):
    #     self.assertEqual(self.prob.get_divisors(22),Set([1, 2, 11]))
    #     self.assertEqual(self.prob.get_divisors(220),Set([1, 2, 5, 10, 11, 110, 22, 55]))
    #     self.assertEqual(self.prob.get_divisors(284),Set([1, 2, 142, 71]))
    #     self.assertEqual(self.prob.get_divisors(512),Set([1, 2, 4, 8, 16, 32, 64, 128, 256]))
    #
    def test_get_divisors(self):
        self.assertEqual(self.prob.get_divisors_brute_force(22),[1, 2, 11])
        self.assertEqual(self.prob.get_divisors_brute_force(220),[1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])
        self.assertEqual(self.prob.get_divisors_brute_force(284),[1, 2, 4, 71, 142])
        self.assertEqual(self.prob.get_divisors_brute_force(512),[1, 2, 4, 8, 16, 32, 64, 128, 256])

    def test_sum_of_divisors(self):
         self.assertEqual(self.prob.sum_of_divisors(22),14)
         self.assertEqual(self.prob.sum_of_divisors(220),284)
         self.assertEqual(self.prob.sum_of_divisors(284),220)






