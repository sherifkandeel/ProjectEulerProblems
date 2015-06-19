__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime
import math

class problem:
    def __init__(self):
        pass


    def generate(self):
        numbers = []
        for i in range(1,10000):
            numbers.append(i*(3*i - 1)/2)
        print numbers[1019], numbers[2166]
        return numbers

    def create_table(self, numbers):
        table = [[0 for x in range(len(numbers))] for x in range(len(numbers))] 
        for i in range(0,len(numbers)):
            for j in range(i+1, len(numbers)):
                num = numbers[i]+numbers[j]
                if self.is_pentagonal(num):
                    table[i][j] = num 

        for i in range(0,len(numbers)):
            for j in range(0,i):
                num =  math.fabs(numbers[i]-numbers[j])
                if self.is_pentagonal(num):
                    table[i][j] = num

        for i in range(0,len(numbers)):
            for j in range(0,len(numbers)):
                if table[i][j] !=0 and table[j][i]!=0:
                    print table[i][j], table[j][i], i, j, math.fabs(numbers[i]-numbers[j])

#                else:
#                    table[i][j]=0
#
#        for row in table:
#            print row
                    

    def is_pentagonal(self, number):
        x1 = (1+(math.sqrt(1+24*number)))/6
        x2 = (1-(math.sqrt(1+24*number)))/6
        if x1>0 and x1==int(x1):
            return True
        elif x2>0 and x2==int(x2):
            return True
        else:
            return False



if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    prob.create_table(prob.generate())
    end = datetime.now()
    print "--- %s  ---" % (str(end-start))




class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass





