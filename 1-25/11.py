__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime
import codecs



class problem:
    def __init__(self):
        self.Matrix = [[0 for x in xrange(20)] for x in xrange(20)]
        self.load_matrix()

    def load_matrix(self):
        with codecs.open('problem_11_matrix') as f:
            row = 0
            for line in f:
                column = 0
                numbers = line.split()
                for number in numbers:
                    self.Matrix[row][column] = int(number)
                    column += 1
                row += 1

        pass

    def vertical_product(self, m, n, w):
        if m+w >= len(self.Matrix) or n >= len(self.Matrix):
            return -1
        product = 1
        for i in range(m, m+w):
            product *= self.Matrix[i][n]
        return product

    def horizontal_product(self, m, n, w):
        if n+w >= len(self.Matrix) or m >= len(self.Matrix):
            return -1 #because it won't make effect anyway
        product = 1
        for i in range(n, n+w):
            product *= self.Matrix[m][i]
        return product

    def diagonal_product(self, m, n, w):
        if m+w >= len(self.Matrix) or n+w >= len(self.Matrix):
            return -1
        product = 1
        for i in range(0, w):
            product *= self.Matrix[m+i][n+i]
        return product

    def other_diagonal_product(self, m, n, w):
        if m+w >=len(self.Matrix) or n-w < -1:
            return -1
        product = 1
        for i in range(0, w):
            product *= self.Matrix[m+i][n-i]
        return product


    def max_product(self, w):
        limit = len(self.Matrix)
        max_product =1
        for i in range(0, limit):
            for j in range (0, limit):
                product = max(self.vertical_product(i, j, w),
                              self.horizontal_product(i, j, w),
                              self.diagonal_product(i, j, w),
                              self.other_diagonal_product(i, j, w))
                print product
                if product > max_product:
                    max_product = product
        return max_product





if __name__ == "__main__":

    start = datetime.now()
    prob = problem()
    print prob.max_product(4)
    end = datetime.now()
    print "--- %d milli seconds ---" % ((end.microsecond-start.microsecond)/1000)



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass

    def test_load_matrix(self):
        self.assertEqual(self.prob.Matrix[0][0], 8)
        self.assertEqual(self.prob.Matrix[5][0], 24)
        self.assertEqual(self.prob.Matrix[19][19], 48)
        pass

    def test_vertical_product(self):
        self.assertEqual(self.prob.vertical_product(5, 0, 4), 24*32*67*24)
        self.assertEqual(self.prob.vertical_product(17, 0, 4), -1)
        self.assertEqual(self.prob.vertical_product(1, 20, 4), -1)
        self.assertEqual(self.prob.vertical_product(1, 2, 0), 1)
        pass

    def test_horizontal_product(self):
        self.assertEqual(self.prob.horizontal_product(5, 0, 4), 24*47*32*60)
        pass

    def test_diagonal_product(self):
        self.assertEqual(self.prob.diagonal_product(0, 0, 4), 8*49*31*23)
        self.assertEqual(self.prob.diagonal_product(15, 0, 5), 88*42*36*29*83)

    def test_other_diagonal_product(self):
        self.assertEqual(self.prob.other_diagonal_product(3, 3, 4), 8*49*31*23)






