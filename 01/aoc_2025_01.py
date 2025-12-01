'''
AoC 2025 Day 1
'''

class AOC:
    def __init__(self, day, filename):
        with open(f'{day:02d}/{filename}') as f:
            self.inp = [line.rstrip() for line in f.readlines()]

    def runprint(self, fun):
        print(fun(self.inp))


def partone(data):
    n, pos = 0, 50
    for line in data:
        dpos = int(line[1:])
        pos += (dpos if line[0] == 'R' else -dpos)
        pos %= 100
        if pos == 0:
            n += 1
    return n
 
def parttwo(data):
    n, pos = 0, 50
    for line in data:
        dpos = int(line[1:])
        if line[0] == 'R':
            n += (pos + dpos) // 100 
            pos += dpos
            pos %= 100
        elif line[0] == 'L':
            n += (dpos - pos) // 100 + (pos != 0)
            pos -= dpos
            pos %= 100
        else:
            raise Exception("Skit in")
    return n


ap = AOC(1,'input')
ap.runprint(partone)
ap.runprint(parttwo)
