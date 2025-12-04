'''
AoC 2025 Day 4
'''

class AOC:
    def __init__(self, day, filename):
        with open(f'{day:02d}/{filename}') as f:
            self.inp = [line.rstrip() for line in f.readlines()]

    def runprint(self, fun):
        print(fun(self.inp))

def fixdata(data):
    s = set()
    for l,line in enumerate(data):
        for k,c in enumerate(line):
            if c == '@':
                s.add((l,k))
    return s

def partone(data):
    s = fixdata(data)
    n_liftable = 0
    for roll in s:
        num = -1
        for k in (-1,0,1):
            for l in (-1,0,1):
                if (roll[0]+l,roll[1]+k) in s:
                    num += 1
        if num < 4:
            n_liftable += 1
    return n_liftable

def parttwo(data):
    s = fixdata(data)
    ns = len(s)
    done = False
    while not done:
        liftable = set()
        for roll in s:
            num = -1
            '''
            for k in (-1,0,1):
                for l in (-1,0,1):
                    if (roll[0]+l,roll[1]+k) in s:
                        num += 1      
            if num < 4:
                liftable.add(roll)
            '''
            # variant with list comprehesion:
            if [(roll[0]+l,roll[1]+k) in s for k in (-1,0,1)  for l in (-1,0,1)].count(True) < 5:
                liftable.add(roll)
        s.difference_update(liftable)
        done = not bool(liftable)
    return ns-len(s)

ap = AOC(4,'input')
ap.runprint(partone)
ap.runprint(parttwo)
