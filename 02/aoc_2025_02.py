'''
AoC 2025 Day 2
'''

class AOC:
    def __init__(self, day, filename):
        with open(f'{day:02d}/{filename}') as f:
            self.inp = [line.rstrip() for line in f.readlines()]

    def runprint(self, fun):
        print(fun(self.inp))

def fix(data):
    ap = data[0].split(',')
    bep = [r.split('-') for r in ap]
    cep = []
    for pair in bep:
        a,b = pair
        while len(b) > len(a):
            cep.append([a, '9'*len(a)])
            a = '1' + '0'*len(a)
        cep.append([a,b])
    return(cep)


def partone(data):
    nydata = fix(data)
    s = 0
    for pair in nydata:
        digs = len(pair[0])
        a, b = (int(c) for c in pair)
        if digs % 2 == 0:
            d = 10**(digs//2) + 1 
            burp = b // d - (a-1) // d
            for k in range(burp):
                invalid_id = ((((a-1)//d) + 1 + k)*d)
                s += invalid_id
    return s
 
def parttwo(data):
    nydata = fix(data)
    s = set()
    for pair in nydata:
        digs = len(pair[0])
        a, b = (int(c) for c in pair)
        for n in range(1,digs):
            if digs % n == 0:
                d = sum(10**(k) for k in range(0,digs,n)) 
                # d: divisor of invalid id, ie number consisting of digs/n repeats of n figures
                burp = b // d - (a-1) // d
                # number of such numbers in the ranga a -- b
                for k in range(burp):
                    # get the invalid ids
                    invalid_id = ((((a-1)//d) + 1 + k)*d)
                    s.add(invalid_id)
    return sum(s)


ap = AOC(2,'input')
ap.runprint(partone)
ap.runprint(parttwo)
