'''
AoC 2025 Day 5
'''

class AOC:
    def __init__(self, day, filename):
        with open(f'{day:02d}/{filename}') as f:
            self.inp = [line.rstrip() for line in f.readlines()]

    def runprint(self, fun):
        print(fun(self.inp))

def fixdata(data):
    range_mode = True
    ranges, ids = [],[]
    for l,line in enumerate(data):
        if line:
            if range_mode:
                rr = tuple(int(a) for a in line.split('-'))
                ranges.append(range(rr[0], rr[1] + 1))
            else:
                ids.append(int(line))
        else:
            range_mode = False
    return ranges, ids

def check(id, ranges):
    for r in ranges:
        if id in r:
            return True
    return False
        


def partone(data):
    ranges, ids = fixdata(data)
    return len(list(filter(lambda x: check(x, ranges), ids)))


def parttwo(data):
    ranges, ids = fixdata(data)
    # merge ranges ...

    return None

ap = AOC(5,'input')
ap.runprint(partone)
ap.runprint(parttwo)
