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
    outs = {}    
    for line in data:
        a, b = line.split(':')
        outs[a] = b.split()
    return outs
            
def count_paths(outs, a, b):
    global tab
    if a == b:
        return 1
    if a not in outs:
        return 1 if a == b else 0
    else:
        if (a,b) in tab:
            return tab[(a,b)]
        else:
            s = 0
            for o in outs[a]:
                s += count_paths(outs, o, b)
            tab[(a,b)] = s
            return s

def partone(data):
    return count_paths(fixdata(data),'you','out')

def parttwo(data):
    fd = fixdata(data)
    if count_paths(fd, 'dac','fft'):
        return count_paths(fd, 'svr','dac') \
            * count_paths(fd, 'dac','fft') \
            * count_paths(fd, 'fft','out')
    else:
        return count_paths(fd, 'svr','fft') \
            * count_paths(fd, 'fft','dac') \
            * count_paths(fd, 'dac','out')
global tab                  
tab = {}
ap = AOC(11,'input')
ap.runprint(partone)
ap = AOC(11,'input')
ap.runprint(parttwo)