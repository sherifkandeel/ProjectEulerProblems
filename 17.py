__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        self.number_dict={}
        self.load_dictionary()
        pass

    def load_dictionary(self):
        self.number_dict[1] = "one"
        self.number_dict[2] = "two"
        self.number_dict[3] = "three"
        self.number_dict[4] = "four"
        self.number_dict[5] = "five"
        self.number_dict[6] = "six"
        self.number_dict[7] = "seven"
        self.number_dict[8] = "eight"
        self.number_dict[9] = "nine"
        self.number_dict[10] = "ten"
        self.number_dict[11] = "eleven"
        self.number_dict[12] = "twelve"
        self.number_dict[13] = "thirteen"
        self.number_dict[14] = "fourteen"
        self.number_dict[15] = "fifteen"
        self.number_dict[16] = "sixteen"
        self.number_dict[17] = "seventeen"
        self.number_dict[18] = "eighteen"
        self.number_dict[19] = "nineteen"
        self.number_dict[20] = "twenty"
        self.number_dict[30] = "thirty"
        self.number_dict[40] = "forty"
        self.number_dict[50] = "fifty"
        self.number_dict[60] = "sixty"
        self.number_dict[70] = "seventy"
        self.number_dict[80] = "eighty"
        self.number_dict[90] = "ninety"
        self.number_dict[100] = "hundred"
        self.number_dict[101] = "hundredand"
        self.number_dict[1000] = "onethousand"


    def F(self, n, strng):
        if len(str(n)) == 4:
            return self.number_dict[1000]
        elif len(str(n)) == 3:
            if n % 100 == 0:
                return self.number_dict[n/100]+self.number_dict[100]
            else:
                _str = self.number_dict[n/100] + self.number_dict[101]
                return self.F(n % 100, _str)
        elif len(str(n)) == 2:
            if n <= 20:
                return strng + self.number_dict[n]
            elif n % 10 == 0:
                return strng + self.number_dict[n]
            else:
                _str = strng + self.number_dict[(n / 10)*10]
                return self.F(n % 10, _str)
        elif len(str(n)) == 1:
            return strng+self.number_dict[n]

    def solve(self, max):
        length = 0
        for i in range(1, max+1):
            length += len(self.F(i, ""))
        return length

if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    print prob.solve(1000)
    end = datetime.now()
    print "--- %s  ---" % (str(end-start))



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass

    def test_F(self):
        self.assertEqual(self.prob.F(15,""), "fifteen")
        self.assertEqual(self.prob.F(115,""), "onehundredandfifteen")
        self.assertEqual(self.prob.F(1000,""), "onethousand")
        self.assertEqual(self.prob.F(25,""), "twentyfive")
        self.assertEqual(self.prob.F(135,""), "onehundredandthirtyfive")
        self.assertEqual(self.prob.F(1,""), "one")
        self.assertEqual(self.prob.F(2,""), "two")
        self.assertEqual(self.prob.F(30,""), "thirty")
        self.assertEqual(self.prob.F(500,""), "fivehundred")
        self.assertEqual(self.prob.F(656,""), "sixhundredandfiftysix")
        self.assertEqual(self.prob.F(342,""), "threehundredandfortytwo")

    def test_solve(self):
        self.assertEqual(self.prob.solve(1000), 21124)






