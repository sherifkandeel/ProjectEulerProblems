__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        self.R= 0
        self.D= 0
        self.count= 0
        self.dict={}
        pass

    def solve(self, G):
        self.R=G
        self.D=G
        self.count=0
        self.F(self.R,self.D)
        return self.count

    def F(self, R, D):
        if self.dict.has_key((R,D)):
            self.count = self.dict[(R,D)]
            return

        if R == 0 and D ==0:
            self.count +=1
            return


        if R != 0:
            self.F(R-1,D)
        # self.dict[(R, D)] = self.count
        if D !=0:
            self.F(R,D-1)
        self.dict[(R, D)] = self.count





if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    print prob.solve(2)
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








# I take it "no backtracking" means we always either increase x or increase y.
#
# If so, we know that in total we will have 40 steps to reach the finish -- 20 increases in x, 20 increases in y.
#
# The only question is which of the 40 are the 20 increases in x. The problem amounts to: how many different ways can you choose 20 elements out of a set of 40 elements. (The elements are: step 1, step 2, etc. and we're choosing, say, the ones that are increases in x).
#
# There's a formula for this: it's the binomial coefficient with 40 on top and 20 on the bottom. The formula is 40!/((20!)(40-20)!), in other words 40!/(20!)^2. Here ! represents factorial. (e.g., 5! = 5*4*3*2*1)
#
# Canceling out one of the 20! and part of the 40!, this becomes: (40*39*38*37*36*35*34*33*32*31*30*29*28*27*26*25*24*23*22*21)/(20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1). The problem is thus reduced to simple arithmatic. The answer is 137,846,528,820.
#
# For comparison, note that (4*3)/(2*1) gives the answer from their example, 6.