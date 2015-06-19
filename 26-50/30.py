__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        pass

    def get_sum_of_powers(self, number, power):
        sumpowers = 0
        while number != 0:
            rem = number % 10
            sumpowers += rem ** power
            number = number / 10
        return sumpowers


    def solve(self, power):
        i = 2
        sum = 0
        while True:
            if self.get_sum_of_powers(i, power) == i:
                print i
                sum += i
            i += 1
            if i > 9999999:
                break
        print "sum %d" % sum


if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    prob.solve(5)
    end = datetime.now()
    print "--- %s  ---" % (str(end - start))


class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()

    pass


    def test_get_sum_of_pwoers(self):
        self.assertEqual(self.prob.get_sum_of_powers(1634, 4), 1634)
        self.assertEqual(self.prob.get_sum_of_powers(8208, 4), 8208)
        self.assertEqual(self.prob.get_sum_of_powers(9474, 4), 9474)



# Actually you can.
# The maximum value for one digit is 9^5 = 59049. We can find out the maximum possible sum for a given number of digits by multiplying 59049 with the number of digits.
# Let's say we're gonna check the number 123456789. That's 9 digits, so the maximum sum would be 9*59049 = 531441, which doesn't even come close to 123456789. So we know we can forget about any number 9-digit number because we'll never be able to reach a big enough sum. And it'll only get worse with larger numbers :)


