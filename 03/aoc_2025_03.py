'''
AoC 2025 Day 3
'''

class AOC:
    def __init__(self, day, filename):
        with open(f'{day:02d}/{filename}') as f:
            self.inp = [line.rstrip() for line in f.readlines()]

    def runprint(self, fun):
        print(fun(self.inp))

def partone(data):
    max_joltage = 0
    for line in data:
        lno, largest = 0, 0
        for k, c in enumerate(line[:-1]):
            if int(c) > largest:
                lno, largest = k, int(c)
        next_largest = 0
        for k, c in enumerate(line[lno+1:]):
            if int(c) > next_largest:
                next_largest = int(c)
        max_joltage += largest*10 + next_largest
    return max_joltage

def get_largest(s, a, b):
    lno, largest = 0, 0
    for k, c in enumerate(s[a:b]):
        if int(c) > largest:
            lno, largest = k, int(c)
    return a+lno, largest
 
def parttwo(data):
    max_joltage = 0
    n = 12
    for line in data:
        lmax = 0
        a, b = 0, len(line) - n + 1
        for k in range(n):
            lno, l = get_largest(line, a, b)
            a, b = lno+1, b + 1
            max_joltage +=  l*10**(n-k-1)
        

    return max_joltage


ap = AOC(3,'input')
ap.runprint(partone)
ap.runprint(parttwo)
