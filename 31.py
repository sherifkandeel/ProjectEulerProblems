__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime
from sets import Set


class problem:
    def __init__(self):
        self.steps = [1, 2, 5, 10, 20, 50, 100, 200]
        self.stepsw = ['1', '2', '5', 'a', 'b', 'c', 'd', 'e']
        self.dict = {}
        self.dict[self.steps[0]] = ['1']
        self.dict[self.steps[1]] = ['11', '2']
        self.dict[self.steps[2]] = ['11111', '122', '1112', '5']
        self.dict[self.steps[3]] = ['1111111111', '1225', '111111112', '55', '11111122', '111115', '11125', '112222',
                                    '1111222', 'a', '22222']
        self.goal = 5
        self.dictionary = set()
        pass


    def get_next_step(self, step):
        arr = list(self.dict[self.steps[step]])

        arr_set = Set()
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                arr_set.add(''.join(sorted(arr[i] + arr[j])))
        # arr_set.add(str(self.steps[step + 1]))


        for stp in self.steps:
            if stp > self.steps[step + 1]: break
            if self.steps[step + 1] % stp != 0: continue
            repeat = self.steps[step + 1] / stp
            toadd = ""
            for i in range(0, repeat):
                toadd += self.convert_to_char(stp)
            arr_set.add(toadd)
            print toadd

        self.dict[self.steps[step + 1]] = arr_set
        # print arr_set
        return len(arr_set)

    def convert_to_char(self, num):
        if num == 10:
            return 'a'
        elif num == 20:
            return 'b'
        elif num == 50:
            return 'c'
        elif num == 100:
            return 'd'
        elif num == 200:
            return 'e'
        else:
            return str(num)


# because it's dynamic programming, only that solution worke,d which I got it from  http://www.mathblog.dk/project-euler-31-combinations-english-currency-denominations/
# my solution ws close but had problems
def something():
    target = 200
    coinSizes = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = {}
    for i in range(0, target + 1):
        ways[i] = 0
    ways[0] = 1

    for i in range(0, len(coinSizes)):
        for j in range(coinSizes[i], target + 1):
            ways[j] += ways[j - coinSizes[i]]

    print ways


if __name__ == "__main__":
    start = datetime.now()
    # prob = problem()
    # # prob.F(0, "")
    # # print prob.dictionary
    # # print len(prob.dictionary)
    # print prob.get_next_step(2)
    # print prob.get_next_step(3)
    # print prob.get_next_step(4)
    # print prob.get_next_step(5)
    # print prob.get_next_step(6)
    # print prob.get_next_step(7)

    # something()

    t = 0
    while t < 0xffffffff:
        t += 1

    end = datetime.now()
    print "--- %s  ---" % (str(end - start))


class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()

    pass





