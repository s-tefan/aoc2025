'''
AoC 2025 Day 10
'''

class AOC:
    def __init__(self, day, filename):
        with open(f'{day:02d}/{filename}') as f:
            self.inp = [line.rstrip() for line in f.readlines()]

    def runprint(self, fun):
        print(fun(self.inp))

def fixdata(data, part=1):
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
            if part == 1:
                for b in press:
                    p ^= 1 << b
            else:
                p = press
            presses.append(p)
        joltage = eval('['+bobs[-1][1:-1]+']')
        val.append((len(lightsyms), lightbits, presses, joltage))
    return val

# Not used in latest version, used in first
def combinations(m,k):
    # return a list of subsets of size k of set m
    if k == 0:
        return [set()]
    s = []
    n = len(m)
    return  [a|{e} for e in m for a in combinations(m-{e},k-1)]

def intcombs(n,k):
    s = []
    for i in range(1,k+1):
        if i == 1:
            s = list([i] for i in range(n))
        else:
            s = [ a + [b] for a in s for b in range(a[-1]+1,n)]
    return s



def presses_needed(nl, light, presses):
    for np in range(1,nl+1):
        #pcombs = combinations(set(presses), np)
        #print(pcombs)
        pcombs = [[presses[i] for i in c] for c in intcombs(len(presses),np)]
        #print(pcombs)
        for ps in pcombs:
            s = light
            for p in ps:
                s ^= p
            if s == 0:
                return np
    raise Exception("Data not compliant")

'''
def presses_needed2(presses, joltage): # fixa...
    print('doing', joltage)
    k = len(presses)
    n = 1
    while True:
        print(n)
        for c in intcombs(n+k-1,k-1):
            jolt=[0]*len(joltage)
            d = [-1] + c + [n+k-1]
            ap = [d[i+1]-d[i]-1 for i in range(k)]
            for j, a in enumerate(presses):
                for b in a:
                    jolt[b] += ap[j]
            if jolt == joltage:
                return n
        n += 1
'''

def jolt(ap, b_counters, nc):
    jolts = [0]*nc
    for j in range(len(b_counters)):
        for c in b_counters[j]:
            jolts[c] += ap[j]
    return jolts

'''
def presses_needed2(presses, joltage): # fixa...
    print('doing', joltage)
    k = len(presses)
    n_pr = [[0]*k]
    nj = len(joltage)
    n = 0
    while n_pr:
        #print(len(n_pr))
        n += 1
        # update
        ny_pr =[]
        for ap in n_pr:
            for i in range(k):
                apa = ap.copy()
                apa[i] += 1
                j = jolt(apa, presses, nj)
                #print(apa, j)
                if j == joltage:
                    return n
                elif all(j[i] <= joltage[i] for i in range(nj)):
                    ny_pr.append(apa)
        n_pr = ny_pr
    raise Exception("No hit")
'''

def presses_needed2(presses, joltage):
    # tänkt att jobba mod p...
    primes = [2,3,5,7,11,13,17,19,23,29]
    m = [[0]*len(presses) for _ in range(len(joltage))]
    print(presses)
    for k, pr in enumerate(presses):
        for j in pr:
            m[j][k] = 1
    print(m)



def partone(data):
    return sum(presses_needed(nl, light, presses) \
        for nl, light, presses, _ in fixdata(data))


def parttwo(data):
    for _, _, presses, joltage in fixdata(data, part = 2):
        a = presses_needed2(presses, joltage) 

ap = AOC(10,'test')
ap.runprint(partone)
ap.runprint(parttwo)