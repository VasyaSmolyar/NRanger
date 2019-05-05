import json
import math
import statistics
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
        self.prepared = []
        self.normal = []
        self.qu = 1 # Дисперсия
        self.ma = 0 # Мат ожидание

    def phi(self, x):
        a = -((x - self.ma) ** 2) / (2 * (self.qu ** 2))
        b = math.sqrt(2 * math.pi) * self.qu
        return b * (math.e ** a)

    def retNum(self, val):
        bit = (self.up - self.down) / self.count
        if val <= self.down:
            return 0
        elif val >= self.up:
            return self.count - 1
        else:
            return int((val - self.down) // bit)

    def setNorm(self):
        self.normal = []
        for period in self.data.values():
            pack = [0 for i in range(self.count)]
            for i in range(self.count):
                c = i-(self.count/2)
                pack[i] = self.phi(((c*self.qu) + (c+1)*self.qu)/2)
            self.normal.append(pack)

    def prepare(self):
        dt = []
        self.prepared = []
        for period in self.data.values():
            pack = [0 for i in range(self.count)]
            for val in period:
                pack[self.retNum(val)] += 1
            s = sum(pack)
            for i in range(len(pack)):
                pack[i] /= s
                pack[i] *= 100
            self.prepared.append(pack)
        self.setNorm()

    def getRects(self, gw, gh):
        dt = []
        for frac in self.prepared:
            for data in frac:
                dt.append(data)
        sw = gw / (len(dt) * 1.5)
        sh = gh / (max(dt) * 1.5)
        w = len(dt) * 3
        old = w
        h = gh / 2 + (max(dt) * 3)
        rects = []
        norms = []
        for frac in self.prepared:
            for data in frac:
                rects.append((w,h - (sh * data),sw,sh * data))
                w += sw
            w += sw
        w = old
        sh = 6 * gh / max(dt)
        for frac in self.normal:
            for data in frac:
                norms.append((w,h - (sh * data),sw,sh * data))
                w += sw
            w += sw
        return (rects,norms)
