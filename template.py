__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        pass



if __name__ == "__main__":
    start = datetime.now()
    prob = problem()

    end = datetime.now()
    print "--- %s  ---" % (str(end-start))



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass





