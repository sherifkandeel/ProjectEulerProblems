__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        self.count = 0
        self.sequence_dict={}
        pass

    def sequence_main_count(self, n):
        if self.sequence_dict.has_key(n):
            return self.sequence_dict[n]
        else:
            num = self.sequence_count(n)
            self.sequence_dict[n]=num
            return num

    def sequence_count(self, n):
        if n == 1: return 1
        self.count += 1
        if n % 2 == 0:
            self.sequence_count(n/2)
        else:
            self.sequence_count(3*n + 1)

        return self.count+1

    def max_chain(self, max):
        max_sequence_count = 0
        max_sequence_number =0
        for i in range(max/2, max):
            if i % 2 ==0: continue
            self.sequence_count(i)
            if self.count > max_sequence_count:
                max_sequence_count = self.count
                max_sequence_number = i
            self.count = 0
        print max_sequence_count
        return max_sequence_number


if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    print prob.max_chain(1000000)
    end = datetime.now()
    print "--- %s  ---" % (str(end-start))



class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()
    pass

    def test_sequence_count(self):
        # self.assertEqual(self.prob.sequence_count(13),10)
        self.assertEqual(self.prob.sequence_count(12),10)



# here's an answer i like
# Not being very clued up on this issue, I decided to attempt a brute force solution. Starting with 500,001 and counting upwards, every odd number was tested. It took 29 hours to find the solution. Reasoning for choosing 500,001 and odd numbers were was based on ->
# every number n under 500,000 has corresponding reverse map 2n in upper half.
# -> Odd number n, reverse maps to and even number in upper half which in turn maps to a number in lower half.
# I would be interested to find out other better methods used to resolve/optimize search for solution.

