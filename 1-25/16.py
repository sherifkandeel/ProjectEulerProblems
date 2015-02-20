__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime

class problem:
    def sums(self,n):
        number=n
        sum = 0
        while number > 0:
            sum+=number%10
            number = number/10
        return sum

    def power_digit(self, power):
        base = 1024
        remainder = power%10
        po = power/10
        return pow(base,po)*pow(2,remainder)


if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    print prob.sums(prob.power_digit(1000))
    end = datetime.now()
    print "--- %s  ---" % (str(end-start))



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass

    def test_power_digit(self):
        self.assertEqual(self.prob.power_digit(10),1024)
        self.assertEqual(self.prob.power_digit(11),2048)
        self.assertEqual(self.prob.power_digit(15),32768)

    def test_sums(self):
        self.assertEqual(self.prob.sums(15),6)
        self.assertEqual(self.prob.sums(327680),26)

    def test_all(self):
        self.assertEqual(self.prob.sums(self.prob.power_digit(15)),26)

