__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        pass

    def is_curious(self, n, d):
        sd = str(d)
        sn = str(n)
        for c in sn:
            if sd.__contains__(c) and c != '0':
                sd = sd.replace(str(c), '', 1)
                sn = sn.replace(str(c), '', 1)
                if len(sn)==0 or len(sd)==0 or sn =='0' or sd =='0' or sn == sd:
                    return False
                new_fraction = float(sn) / float(sd)
                if new_fraction == float(n) / float(d):
                    print n, d, float(n) / float(d), sn, sd, new_fraction
                    return True
        return False

    def solve(self):
        total = 1
        for n in range(10, 100):
            for d in range(n, 100):

                if self.is_curious(n, d):
                    print n, d
                    total *= float(n) / float(d)
        print total


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

    def test_is_curious(self):
        self.assertFalse(self.prob.is_curious(24, 48))
        self.assertFalse(self.prob.is_curious(56, 66))
        self.assertFalse(self.prob.is_curious(12, 24))
        self.assertFalse(self.prob.is_curious(23, 45))
        self.assertTrue(self.prob.is_curious(49, 98))
