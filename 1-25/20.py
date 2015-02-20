__author__ = 'Sherif'

prod = 1
for i in range (1, 101):
    prod *= i
print sum(int(i) for i in str(prod))