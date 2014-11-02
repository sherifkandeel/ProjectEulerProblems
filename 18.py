__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime
import codecs

class problem:
    def __init__(self):
        self.size = 15
        self.matrix = [[0 for x in xrange(self.size)] for x in xrange(self.size)]
        self.fill_matrix()

        pass

    def fill_matrix(self):
        with codecs.open("problem_18_tree") as f:
            y = 0
            for line in f:
                x = 0
                numbers = line.split(' ')
                for num in numbers:
                    self.matrix[y][x] = int(num)
                    x += 1
                    # if x > 1 and x< y*2-1:
                    #     self.matrix[y][x] = int(num)
                    #     x += 1
                y += 1


    def brute_force(self):
        posSolutions = pow(2, self.size - 1)
        print posSolutions
        largestSum = 0

        for i in range(0,posSolutions):
            tempSum = self.matrix[0][0]
            index = 0
            for j in range(0, self.size-1):
                index = index + (i >> j & 1)
                tempSum += self.matrix[j+1][index]
            if tempSum >largestSum:
                largestSum = tempSum

        return largestSum






if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    print prob.brute_force()

    end = datetime.now()
    print "--- %s  ---" % (str(end-start))



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass





