from decimal import Decimal, localcontext
from fractions import Fraction

__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        pass

    def run(self):
        max_d = -1
        max_val = -1
        for i in range(1, 1001):
            f = self.get_fraction(Fraction(1, i), 2000)
            # x = self.get_recurring_size(f)
            # print "trying %s" % str(f)[2:]
            x = self.f(str(f)[2:], 0, 1)
            # print "%s produces %f recurrences" % (i, x)
            if x >= max_val:
                max_val = x
                max_d = i
        print "d is %f and recurring count is %f " % (max_d, max_val)

    def get_fraction(self, f, digits):
        assert (f.imag == 0)
        # Automatically reset the Decimal settings
        with localcontext() as ctx:
            ctx.prec = digits
            return (Decimal(f.numerator) / Decimal(f.denominator))


    def all_empty(self, n):
        # print n
        n = n[1:-1]
        for c in n:
            if c != "":
                return False
        return True

    def f(self, n, start, end):

        if start >= len(n) - 1:
            return 0

        if end >= len(n):
            start += 1
            end = start + 1
            return self.f(n, start, end)

        if self.all_empty(n.split(n[start:end])):
            return len(n[start:end])

        return self.f(n, start, end + 1)


if __name__ == "__main__":
    start = datetime.now()
    f = Fraction(1, 312)
    prob = problem()
    # print prob.get_fraction(f, 1000)
    prob.run()
    end = datetime.now()
    print "--- %s  ---" % (str(end - start))


class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()

    pass

    def test_is_array_eqaul(self):
        self.assertTrue(self.prob.is_array_equal(["1234", "1234"]))
        self.assertTrue(self.prob.is_array_equal(["1234", "1234", "1234"]))
        self.assertFalse(self.prob.is_array_equal(["1234", "1234", "1"]))

    def test_recurring_size(self):
        self.assertEqual(self.prob.get_recurring_size("0.66666666"), 1)
        self.assertEqual(self.prob.get_recurring_size("0.123123123"), 3)
        self.assertEqual(self.prob.get_recurring_size("0.8123123123"), 3)
        self.assertEqual(self.prob.get_recurring_size("0.0.003205128205128205128205128205128205128205128205128205128"),
                         6)
        self.assertEqual(self.prob.get_recurring_size("0.5"), 0)

    def test_run(self):
        self.prob.run()

    def test_F(self):
        n = "1234123412341234"
        self.assertEqual(self.prob.f(n, 0, 1), 4)



