__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime
import codecs
import math

class problem:
    def __init__(self):
        pass

    def get_number(self, st):
        tot = 0
        for c in st:
            tot += (ord(c) - 64)
        return tot

    def index_words(self):
        dict = {}
	with codecs.open('C:\Work\ProjectEulerProblems\p042_words.txt') as f:
            for line in f:
		    s = line
        s = s.replace('"','')
        arr = s.split(",")
	return arr


    def is_triangle_number(self, c):
	x1 = (-1+math.sqrt(1+4*2*c))/2
	x2 = (-1-math.sqrt(1+4*2*c))/2
#	print x1,x2
	if x1>0 and x1==int(x1):
	    return True
    elif x2>0 and x2==int(x2):
	    return True
	else:
	    return False

    def is_triangle_word(self, word):
	number = self.get_number(word)
        return self.is_triangle_number(number)

    def solve(self):
	count = 0 
	words = self.index_words()
	for word in words:
		if self.is_triangle_word(word):
			count+=1
	print count




if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    print prob.solve()
    end = datetime.now()
    print "--- %s  ---" % (str(end - start))

class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()

    def test_get_number(self):
        self.assertEqual(self.prob.get_number("AB"), 3)
        self.assertEqual(self.prob.get_number("B"), 2)

    def test_triangle_number(self):
	self.assertTrue(self.prob.is_triangle_number(55))




