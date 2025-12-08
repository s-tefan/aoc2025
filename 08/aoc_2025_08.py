'''
AoC 2025 Day 8
'''

class AOC:
    def __init__(self, day, filename):
        with open(f'{day:02d}/{filename}') as f:
            self.inp = [line.rstrip() for line in f.readlines()]

    def runprint(self, fun):
        print(fun(self.inp))

def fixdata(data):
    return [tuple(int(x) for x in line.split(',')) for line in data]
            
def dist2(p,q):
    return sum((x-y)**2 for x,y in zip(p,q))

def partone(data):
    box_pos_list = fixdata(data)
    n = len(box_pos_list)

    dd = dict()
    for k in range(n):
        for m in range(k+1, n):
            d2 = dist2(box_pos_list[k], box_pos_list[m])
            dd[(k,m)] = d2
    ds = sorted(dd, key=dd.get)
    shortest = ds[:1000]
    circuits = []
    for p in shortest:
        ap = []
        for c in circuits:
            if p[0] in c or p[1] in c:
                ap.append(c)
        if len(ap) == 0:
            circuits.append(set(a for a in p))
        elif len(ap) == 1:
            ap[0] |= set(a for a in p)
        elif len(ap) == 2:
            ap[0] |= ap[1]
            circuits.remove(ap[1])
        else:
            raise Exception("Vafan?")

    csizes = [len(c) for c in circuits]
    csizes.sort(reverse=True)
    return csizes[0]*csizes[1]*csizes[2]

# partone do not record singleton circuits, parttwo do

def parttwo(data):
    box_pos_list = fixdata(data)
    n = len(box_pos_list)
    circuits = [{k} for k in range(n)]
    dd = dict()
    for k in range(n):
        for m in range(k+1, n):
            d2 = dist2(box_pos_list[k], box_pos_list[m])
            dd[(k,m)] = d2
    ds = sorted(dd, key=dd.get)
    for p,q in ds:
        ap = []
        for c in circuits:
            if p in c:
                ap.append(c)
            if q in c:
                ap.append(c)
        if len(ap) == 0:
            pass
        elif len(ap) == 1:
            pass
        elif len(ap) == 2:
            if ap[0] != ap[1]:
                ap[0] |= ap[1]
                circuits.remove(ap[1])
        else:
            raise Exception("Vafan?")
        if len(circuits) == 1:
            return box_pos_list[p][0]*box_pos_list[q][0]

ap = AOC(8,'input')
ap.runprint(partone)
ap.runprint(parttwo)