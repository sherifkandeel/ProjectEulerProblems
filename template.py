__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime


class problem:



if __name__ == "__main__":
    start = datetime.now()
    prob = problem()

    end = datetime.now()
    print "--- %d milli seconds ---" % ((end.microsecond-start.microsecond)/1000)



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass





