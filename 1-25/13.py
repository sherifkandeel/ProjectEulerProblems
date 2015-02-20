__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime
import codecs

class problem:

    def __init__(self):
        self.numbers = []

    pass


    def add_numbers(self):
        with codecs.open('problem_13_numbers') as f:
            result=0
            for line in f:
                result += long(line[0:11])
        return (str(result))[0:10]




if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    print prob.add_numbers()
    end = datetime.now()
    print "--- %d milli seconds ---" % ((end.microsecond-start.microsecond)/1000)



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass






