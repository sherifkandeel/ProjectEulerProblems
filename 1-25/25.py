__author__ = 'sherif'

Fn1 = 1
Fn2 = 1
F = 0
cnt = 2
while True:
    F = Fn1 + Fn2
    Fn2 = Fn1
    Fn1 = F
    cnt = cnt + 1
    if len(str(F)) >= 1000:
        print cnt
        break


# Fibonacci terms converge to (n)*Phi=(n+1), where Phi is the
#  Golden Ratio (1+sqrt5)/2.
# I reasoned that there is an nth term that is smaller than 10^999
#  with the corresponding nth+1 term bigger than 10^999.