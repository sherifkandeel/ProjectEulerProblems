dividers = set()
dict = {}
for m in range(1, 99):
    for n in range(1, m):
        a = (m * m - n * n)
        b = 2 * m * n
        c = (m * m + n * n)
        tot = a + b + c
        if dict.has_key(tot):
            dict[tot] += 1
        else:
            dict[tot] = 1
        if a % 51 == 0 or b % 51 == 0 or c % 51 == 0:
            if a % 51 == 0:
                div = a / 51
                if div == 0: div = 1
                dividers.add(div)
                print a / div, b / div, c / div
            elif b % 51 == 0:
                div = b / 51
                if div == 0: div = 1
                dividers.add(div)
                print a / div, b / div, c / div
            elif c % 51 == 0:
                div = c / 51
                if div == 0: div = 1
                dividers.add(div)
                print a / div, b / div, c / div
print dividers
