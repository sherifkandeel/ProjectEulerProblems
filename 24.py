def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p
        for i in range(low + 1, len(xs)):
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p
            xs[low], xs[i] = xs[i], xs[low]


result = []
for p in permute([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    result.append(str(p).replace('[', '').replace(',', '').replace(' ', '').replace(']', ''))

result.sort()

print result[999999]