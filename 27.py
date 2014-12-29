import codecs

__author__ = 'sherif'


class problem:
    def __init__(self):
        self.primes = []
        self.load_primes()
        pass

    def load_primes(self):
        with codecs.open('primes1m.txt') as f:
            for line in f:
                self.primes.append(int(line))
        pass

    def solve(self):
        max = 0
        maxa=0
        maxb=0
        for a in range (1,1001):
            for b in range (1,1001):
                cnt = 1
                while True:


