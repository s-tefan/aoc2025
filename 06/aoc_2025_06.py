'''
AoC 2025 Day 6
'''

class AOC:
    def __init__(self, day, filename):
        with open(f'{day:02d}/{filename}') as f:
            #self.inp = [line.rstrip() for line in f.readlines()]
            # just stripping the newline today
            self.inp = [line[:-1] for line in f.readlines()]

    def runprint(self, fun):
        print(fun(self.inp))

def fixdata(data):
    return [line.split() for line in data]

        
def partone(data):
    rows = fixdata(data)
    ops = rows[-1]
    acc = [1 if c == '*' else 0 for c in ops]
    for row in rows[:-1]:
        for k, c in enumerate(row):
            if ops[k] == '*':
                acc[k] *= int(c)
            else:
                acc[k] += int(c)
    return sum(acc)



def parttwo(data):
    ops = data[-1].split()
    acc = [1 if c == '*' else 0 for c in ops]
    cacc = ['' for c in data[0]]
    for row in data[:-1]:
        for k, c in enumerate(row):
            cacc[k] += c
    collist = []
    stack = []
    for s in cacc:
        if s.strip() == '':
            if stack:
                collist.append(stack)
            stack = []
        else:
            stack.append(s)
    if stack:
        collist.append(stack)
    for k, nums in enumerate(collist):
        for s in nums:
            if ops[k] == '*':
                acc[k] *= int(s)
            else:
                acc[k] += int(s)    
    return sum(acc)

ap = AOC(6,'input')
ap.runprint(partone)
ap.runprint(parttwo)

