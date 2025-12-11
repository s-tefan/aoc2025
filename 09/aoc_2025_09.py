'''
AoC 2025 Day 9
'''

class AOC:
    def __init__(self, day, filename):
        with open(f'{day:02d}/{filename}') as f:
            self.inp = [line.rstrip() for line in f.readlines()]

    def runprint(self, fun):
        print(fun(self.inp))

def fixdata(data):
    return [tuple(int(x) for x in line.split(',')) for line in data]
            


def partone(data):
    coords = fixdata(data)
    largest = 0
    for k, p in enumerate(coords):
        for m, q in enumerate(coords[:k-1]):
            largest = max(largest, int((abs(p[0]-q[0])+1)*(abs(p[1]-q[1])+1)))
    return largest

def parttwo(data):
    return None

ap = AOC(9,'input')
ap.runprint(partone)
ap.runprint(parttwo)