__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        pass

    def is_pandigital(self, j, k, l):
        s = str(j) + str(k) + str(l)
        if len(s) < 9 or len(s) > 9:
            return False
        if s.__contains__("1") and s.__contains__("2") and s.__contains__("2") and s.__contains__(
                "3") and s.__contains__("4") and s.__contains__("5") and s.__contains__("6") and s.__contains__(
                "7") and s.__contains__("8") and s.__contains__("9"):
            return True
        return False

    def total_count(self, j, k, l):
        return len(str(j) + str(k) + str(l))

    def solve(self):
        count = 0
        sum = 0
        sums = {}
        for j in range(1, 9999):
            for k in range(1, 99):
                l = j * k
                if self.is_pandigital(j, k, l):
                    if sums.has_key(l):
                        continue
                    sums[l] = 1
                    count += 1
                    sum += l
                    print j, k, l
        print count
        print sum


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

    def test_is_pandigital(self):
        self.assertTrue(self.prob.is_pandigital(123, 456, 789))
        self.assertFalse(self.prob.is_pandigital(123, 3456, 789))
        self.assertFalse(self.prob.is_pandigital(123, 456, 78))



# We are searching for a sequence of numbers+answer A+B=C with lengths a+b+c = 9.
#
# Since only numbers of length a and b can make products of length (a+b)[lt]c[lt](a+b-1), and total length a+b+c must be 9, we can conclude the following;
#
# a+b+(a+b+f) = 9     (0[lt]f[lt]1)
# 2a+2b = 9-f
# a+b = (9-f)/2
# 4.5 [lt] a+b [lt] 5
#
# So, in the equation A+B=C given a number A of length 1[lt]a[lt]5, the other number B must have length 4.5-a [lt] b [lt] 5-a
#
# Using this property, I made a loop for number A, counting to 4 digits, and a loop B within which counts numbers of length 4.5-length(A) to 5-length(A)
#
# I used a table to prevent double counts. (very memory unefficient, but fast)