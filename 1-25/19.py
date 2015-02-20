__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        self.months = {}
        pass

    def load_months(self, leap):
        self.months[1] = 1
        self.months[2] = 32
        self.months[3] = 60 + leap
        self.months[4] = 91 + leap
        self.months[5] = 121 + leap
        self.months[6] = 152 + leap
        self.months[7] = 182 + leap
        self.months[8] = 213 + leap
        self.months[9] = 244 + leap
        self.months[10] = 274 + leap
        self.months[11] = 305 + leap
        self.months[12] = 335 + leap

    def evaluate(self):
        sunday = 7
        leap =0
        good_sundays = 0

        for year in range (0, 101):
            if year > 0 and year % 4 == 0:
                # print 1900+year
                leap = 1
            else:
                leap = 0
            self.load_months(leap)
            while sunday < 365+leap:
                for m in self.months:
                    if sunday == self.months[m] and year > 0:
                        # print sunday
                        good_sundays += 1
                sunday += 7
            sunday = sunday - (365+leap)
            print good_sundays
        return good_sundays

if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    print prob.evaluate()
    end = datetime.now()
    print "--- %s  ---" % (str(end-start))


class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass

    def test_run(self):
        print self.prob.evaluate()
#
#
# for some reason something like this works:
#     I just computed 1200/7 = 171 :)