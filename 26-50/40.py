__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        pass

    def solve(self):
        strn = ""
        for i in range(0, 200000):
            strn += str(i)
        print len(strn)
        print strn[12]
        print int(strn[1]) * int(strn[10]) * int(strn[100]) * int(strn[1000]) * int(strn[10000]) * int(strn[100000]) * int(strn[1000000])


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



# I did it in C++ and outputed the results, since it is the natural number progression :
#
# pos => number (bracket to see the exact number pos)
#
# 1 => 1
# 10 => [1]0
# 100 => [5]5
# 1000 => [3]70
# 10000 => 27[7]7
# 100000 => [2]2222
# 1000000 => [1]85185
#
# THEN : 1*1*5*3*7*2*1 = 210

