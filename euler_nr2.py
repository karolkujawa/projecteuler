from math import sqrt


def F(n):
    return ((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))


def F():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b


def SF(startNr, endNr):
    for cur in F():
        if cur > endNr:
            return
        if cur >= startNr:
            yield cur


for i in SF(0, 4000000):
   if i % 2 == 0:
        print(i)
   else:
       continue
