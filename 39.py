__author__ = 'Sherif'
from unittest import TestCase
from datetime import datetime


class problem:
    def __init__(self):
        pass

    def hcf(self, n1, n2):
        while n1 * n2:
            if n1 > n2:
                n1 %= n2
            else:
                n2 %= n1
        return max(n1, n2)

    def coprime(self, n1, n2):
        return self.hcf(n1, n2) == 1


    def solve(self):
        dict = {}
        for m in range(1, 22):
            for n in range(1, m):
                for k in range(1, 99):
                    a = k * (m * m - n * n)
                    b = k * 2 * m * n
                    c = k * (m * m + n * n)
                    tot = a + b + c
                    if tot > 1000:
                        break
                    if a < 0 or b < 0 or c < 0:
                        continue

                    if m % 2 == 0 and n % 2 == 0:
                        continue

                    if m % 2 != 0 and n % 2 != 0:
                        a /= 2
                        b /= 2
                        c /= 2
                    if not self.coprime(m, n):
                        continue

                    tot = a + b + c
                    arr = []
                    arr.append(a)
                    arr.append(b)
                    arr.append(c)
                    arr.sort()
                    if dict.has_key(tot):

                        dict[tot].add(str(arr))
                    else:
                        dict[tot] = set()
                        dict[tot].add(str(arr))

        xmaxp = 0
        xmaxv = 0
        for i in dict.keys():
            if len(dict[i]) > xmaxv:
                xmaxv = len(dict[i])
                xmaxp = dict[i]
        print xmaxv, xmaxp


if __name__ == "__main__":
    start = datetime.now()
    prob = problem()
    prob.solve()
    end = datetime.now()
    print "--- %s  ---" % (str(end - start))


class problemTest(TestCase):
    def setUp(self):
        self.prob = problem()

    pass





