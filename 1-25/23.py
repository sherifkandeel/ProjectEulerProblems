__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        pass

    # def get_divisors_sum(self, number):
    # sum = 0
    # for c in range(1, number/2+1):
    # if number % c == 0:
    # sum += c
    # return sum


    def factors(self, n):
        return set(reduce(list.__add__,
                          ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


    def get_divisors_sum(self, n):
        set = self.factors(n)
        sum = -n
        for c in set:
            sum += c
        return sum

    def get_abundants(self):
        limit = 28123
        abundants = []
        for num in range(1, limit):
            if num < self.get_divisors_sum(num):
                abundants.append(num)
        return abundants

    def get_sums_less_than_limit(self, abundants, limit):
        list_of_sums_of_abundants = set()
        for i in abundants:
            for j in abundants:
                if i + j < limit:
                    list_of_sums_of_abundants.add(i + j)
        return list_of_sums_of_abundants

    def get_sum_of_other_ints(self, limit):
        sum = 0
        excluded = self.get_sums_less_than_limit(self.get_abundants(), limit)
        for i in range(1, limit):
            if excluded.__contains__(i):
                continue
            sum+=i
        return sum


if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    print prob.get_sum_of_other_ints(28123)
    # print prob.factors(28)
    end = datetime.now()
    print "--- %s  ---" % (str(end - start))


class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()

    pass

    def test_get_divisors(self):
        self.assertEqual(self.prob.get_divisors_sum(28), 28)




