__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        self.R=""
        self.D=""
        self.count=0
        pass

    def solve(self, G):
        self.R=""
        self.D=""
        self.count=0
        for i in range(0,G):
            self.R += '-'
            self.D += '-'
        self.F(self.R,self.D)
        return self.count

    def F(self, R, D):
        if len(R) == 0 and len(D) ==0:
            self.count +=1
            return
        if len(R) != 0:
            self.F(R[:-1],D)
        if len(D) !=0:
            self.F(R,D[:-1])





if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    print prob.solve(15)
    end = datetime.now()
    print "--- %s  ---" % (str(end-start))



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass

    def test_solve(self):
        self.assertEqual(self.prob.solve(2),6)
        self.assertEqual(self.prob.solve(3),20)
        self.assertEqual(self.prob.solve(4),70)






