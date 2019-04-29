import json
from errors import NError

class NEngine():
    def __init__(self,fname,down,up,count):
        self.fname = fname
        try:
            f = open(fname,'r')
            self.data = json.load(f)
        except (json.JSONDecodeError, OSError):
            raise NError("Ошибка чтения файла")
        self.down = down
        self.up = up
        self.count = count
        self.prepared = [[1,2,3,2,1],[4,2,6,1,3],[2,4,6,4,1],[3,4,4]]

    def getRects(self, gw, gh):
        dt = []
        for frac in self.prepared:
            for data in frac:
                dt.append(data)
        sw = gw / (len(self.prepared) * 7.5)
        sh = gh / 10
        w = 0
        h = gh / 2 + (sw*max(dt))
        rects = []
        for frac in self.prepared:
            for data in frac:
                rects.append((w,h - (sh * data),sw,sh * data))
                w += sw
            w += sw
        return rects
