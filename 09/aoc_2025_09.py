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

# part two does not work yet
def parttwo(data):
    coords = fixdata(data)
    areas = []
    h_edges, v_edges = [], []
    for k, p in enumerate(coords):
        q = coords[(k-1)%len(coords)]
        if p[0] == q[0]:
            h_edges.append((p[0],min(p[1],q[1]),max(p[1],q[1])))
        else:
            v_edges.append((p[1],min(p[0],q[0]),max(p[0],q[0])))

    for k, p in enumerate(coords):
        for m, q in enumerate(coords[:k-1]):
            c_min, c_max = (min(p[0],q[0]),min(p[1],q[1])), (max(p[0],q[0]),max(p[1],q[1]))

            if not any( \
                (v[0] in range(c_min[0]+1,c_max[0])) and (v[1] < c_max[1] or v[2] >= c_min[1]) \
                for v in v_edges) or \
                not any( \
                (h[1] in range(c_min[1]+1,c_max[1]) and (h[1] <= c_max[0] or h[2] >= c_min[0])) \
                for h in h_edges):
                areas.append(int((abs(p[0]-q[0])+1)*(abs(p[1]-q[1])+1)))
                print(p,q)

            '''


            if not any(c[0] in range(min(p[0],q[0])+1,max(p[0],q[0])) and \
                        c[1] in range(min(p[1],q[1])+1,max(p[1],q[1])) \
                            for c in coords):
                areas.append(int((abs(p[0]-q[0])+1)*(abs(p[1]-q[1])+1)))
                print(p,q)
            '''
    return max(areas)

ap = AOC(9,'test')
ap.runprint(partone)
ap.runprint(parttwo)