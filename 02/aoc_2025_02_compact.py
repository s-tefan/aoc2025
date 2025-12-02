'''
AoC 2025 Day 2
Compactified version
'''
import time


class AOC:
    def __init__(self, day, filename):
        with open(f'{day:02d}/{filename}') as f:
            self.inp = [line.rstrip() for line in f.readlines()]

    def runprint(self, fun):
        print(fun(self.inp))

def fix(data):
    cep = []
    for a,b in (r.split('-') for r in data[0].split(',')):
        while len(b) > len(a):
            cep.append([a, '9'*len(a)])
            a = '1' + '0'*len(a)
        cep.append([a,b])
    return(cep)

def partone(data):
    s = 0
    for pair in fix(data):
        digs = len(pair[0])
        a, b = (int(c) for c in pair)
        if digs % 2 == 0:
            d = 10**(digs//2) + 1 
            for k in range(b // d - (a-1) // d):
                s += ((((a-1)//d) + 1 + k)*d)
    return s
 
def parttwo(data):
    s = set()
    for pair in fix(data):
        digs = len(pair[0])
        a, b = (int(c) for c in pair)
        for n in range(1,digs):
            if digs % n == 0:
                d = sum(10**(k) for k in range(0,digs,n)) 
                for k in range(b // d - (a-1) // d):
                    s.add(((((a-1)//d) + 1 + k)*d))
    return sum(s)

t0 = time.process_time_ns()
ap = AOC(2,'input')
t1 = time.process_time_ns()
ap.runprint(partone)
t2 = time.process_time_ns()
ap.runprint(parttwo)
t3 = time.process_time_ns()
print(t1-t0,t2-t1,t3-t2,'ns')