'''
AoC 2025 Day 7
'''

class AOC:
    def __init__(self, day, filename):
        with open(f'{day:02d}/{filename}') as f:
            self.inp = [line.rstrip() for line in f.readlines()]

    def runprint(self, fun):
        print(fun(self.inp))

def fixdata(data):
    spos = data[0].index('S')
    d = []
    for line in data[1:]:
        a = [k for k,c in filter(lambda x: x[1]=='^', enumerate(line))]
        if a:
            d.append(a)
    return len(data[0]), spos, d
            
        
def partone(data):
    n, spos, splitlist = fixdata(data)
    beams = {spos}
    n_splits = 0
    for splits in splitlist:
        for split in splits:
                if split in beams:
                    n_splits += 1
                    beams.remove(split)
                    if split > 0:
                        beams.add(split-1)
                    if split <= n-1:
                        beams.add(split+1)
    return n_splits


def parttwo(data):
    n, spos, splitlist = fixdata(data)
    beams = {spos: 1}
    for splits in splitlist:
        for split in splits:
                if split in beams:
                    if split > 0:
                        if split-1 in beams:
                            beams[split-1] += beams[split]
                        else:
                            beams[split-1] = beams[split]
                    if split <= n-1:
                        if split+1 in beams:
                            beams[split+1] += beams[split]
                        else:
                            beams[split+1] = beams[split]
                    del beams[split]
    return sum(beams.values())


ap = AOC(7,'input')
ap.runprint(partone)
ap.runprint(parttwo)

