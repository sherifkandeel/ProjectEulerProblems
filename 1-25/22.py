from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        pass

    def read_to_list(self, filename):
        f = open('problem_22_names', 'r')
        str = ""
        for line in f:
            str = line
        str = str.replace('"', '')
        mylist = str.split(',')
        mylist.sort()
        return mylist

    def caluclate_value(self, name):
        val = 0
        for c in name:
            val += ord(c) - 64
        return val


def run():
    prob = problem()
    mylst = prob.read_to_list("problem_22_names")

    score = 0
    order = 1
    for name in mylst:
        score += order * prob.caluclate_value(name)
        order += 1
    print score


if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    run()
    end = datetime.now()
    print "--- %s  ---" % (str(end - start))


class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()

    pass

    def test_read_to_list(self):
        mylist = []
        mylist.append("adriana")
        mylist.append("anna")
        mylist.append("jay-z")
        mylist.append("z")

        self.assertEqual(self.prob.read_to_list("problem_22_names"), mylist)


    def test_calculate_value(self):
        self.assertEqual(self.prob.caluclate_value('COLIN'), 53)
