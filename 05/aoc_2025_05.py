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

def normalize(ranges):
    ranges.sort(key = lambda x: x.start)
    k=0
    while True:
        if k == len(ranges)-1:
            return
        if ranges[k+1].start in ranges[k]:
            ranges[k] = range(ranges[k].start,max(ranges[k].stop,ranges[k+1].stop))
            ranges.pop(k+1)
        else:
            k += 1
        
def partone(data):
    ranges, ids = fixdata(data)
    return len(list(filter(lambda x: check(x, ranges), ids)))

def parttwo(data):
    ranges, _ = fixdata(data)
    normalize(ranges)
    return sum(len(r) for r in ranges)

ap = AOC(5,'input')
ap.runprint(partone)
ap.runprint(parttwo)

