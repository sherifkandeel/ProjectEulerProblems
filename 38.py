__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime
from itertools import permutations


class problem:
    def __init__(self):
        pass

    def get_permutations_sorted(self, s, o):
        perms = [''.join(p) for p in permutations(s)]
        perms.sort()
        if o == 1:
            perms.reverse()
        return perms

    def check_pandigital(self, number):
        formulated_number = ""
        original = set("123456789")
        for i in range(1, 10):
            if self.is_rightful(original, str(number * i)):
                original = self.get_difference(original, set(str(number * i)))
                formulated_number += str(number * i)
                # print number * i, original
            elif len(original) == 0:
                return formulated_number
                # return True
            else:
                return "False"

    def solve(self):
        solution = ""
        for i in range(1, 99999):
            st = self.check_pandigital(i)
            if st != "False":
                solution = st
        print solution

    def is_rightful(self, original, new):
        if len(set(new)) != len(new):
            return False
        new = set(new)
        return new.issubset(original)

    def get_difference(self, original, new):
        for i in new:
            original.remove(i)
        return original


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

    def test_get_permutations(self):
        self.assertEqual(self.prob.get_permutations_sorted("so", 0), ['os', 'so'])
        self.assertEqual(self.prob.get_permutations_sorted("123", 0), ['123', '132', '213', '231', '312', '321'])
        # self.assertEqual(self.prob.get_permutations_sorted("so"), ['so', 'os'])



