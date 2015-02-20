__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime


class problem:
    def is_valid(self, b, c):
        eq = 1000000 - 2000 * b - 2000 * c + 2 * b * c + 2 * b * b #eqn driven from the two inputs
        if (eq == 0):
            return True
        return False


    def check(self):
        for b in range(1, 1001):
            for c in range(1, 1001):
                if self.is_valid(b, c):
                    a = 1000 - b - c
                    if a > 0 and a != 0:
                        print "valid a = %d , b = %d , c = %d" %(a, b, c)
                        print "abc is %d" % (a*b*c)






if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    prob.check()
    end = datetime.now()
    print "--- %d milli seconds ---" % ((end.microsecond-start.microsecond)/1000)



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass


# Without programming:
#
# a= 2mn; b= m^2 -n^2; c= m^2 + n^2;
# a + b + c = 1000;
#
# 2mn + (m^2 -n^2) + (m^2 + n^2) = 1000;
# 2mn + 2m^2 = 1000;
# 2m(m+n) = 1000;
# m(m+n) = 500;
#
# m>n;
#
# m= 20; n= 5;
#
# a= 200; b= 375; c= 425;



