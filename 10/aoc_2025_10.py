'''
AoC 2025 Day 10
'''

class AOC:
    def __init__(self, day, filename):
        with open(f'{day:02d}/{filename}') as f:
            self.inp = [line.rstrip() for line in f.readlines()]

    def runprint(self, fun):
        print(fun(self.inp))

def fixdata(data):
    val = []
    for line in data:
        bobs = line.split()
        lightsyms = bobs[0][1:-1]
        lightbits = 0
        for x in reversed(lightsyms):
            lightbits <<= 1
            if x == '#':
                lightbits |= 1
        presses = []
        for a in bobs[1:-1]:
            press = eval(a)
            p = 0
            if isinstance(press, int):
                press = (press,)
            for b in press:
                p ^= 1 << b
            presses.append(p)
        joltage = bobs[-1]
        val.append((len(lightsyms), lightbits, presses, joltage))
    return val

def combinations(m,k):
    # return a list of subsets of size k of set m
    if k == 0:
        return [set()]
    s = []
    n = len(m)
    return  [a|{e} for e in m for a in combinations(m-{e},k-1)]


def presses_needed(nl, light, presses):
    for np in range(1,nl+1):
        pcombs = combinations(set(presses), np)
        for ps in pcombs:
            s = light
            for p in ps:
                s ^= p
            if s == 0:
                return np
    raise Exception("Data not compliant")



def partone(data):
    return sum(presses_needed(nl, light, presses) \
        for nl, light, presses, _ in fixdata(data))


def parttwo(data):
    return None


ap = AOC(10,'input')
ap.runprint(partone)
ap.runprint(parttwo)