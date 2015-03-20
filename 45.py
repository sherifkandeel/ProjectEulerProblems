__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime
import math

class problem:
    def __init__(self):
        pass

    def is_pentagonal_number(self, number):
        x1 = (1+(math.sqrt(1+24*number)))/6
        x2 = (1-(math.sqrt(1+24*number)))/6
        if x1>0 and x1==int(x1):
            return True
        elif x2>0 and x2==int(x2):
            return True
        else:
            return False

    def is_triangle_number(self, c):
	x1 = (-1+math.sqrt(1+4*2*c))/2
	x2 = (-1-math.sqrt(1+4*2*c))/2
	if x1>0 and x1==int(x1):
	    return True
	elif x2>0 and x2==int(x2):
	    return True
	else:
	    return False

    def is_hexagonal_number(self, c):
	x1 = (1+math.sqrt(1+4*2*c))/4
	x2 = (1-math.sqrt(1+4*2*c))/4
	if x1>0 and x1==int(x1):
	    return True
	elif x2>0 and x2==int(x2):
	    return True
	else:
	    return False

    def solve(self):
        gotit = 0
        number = 0
        n = 0
	while True:	
            n+=1
            number = n*(2*n-1)
            if self.is_pentagonal_number(number):
                if self.is_triangle_number(number):
                    print number
                    gotit+=1
                    if gotit==3:
                        break
                    

if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    prob.solve()
    end = datetime.now()
    print "--- %s  ---" % (str(end-start))



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass

