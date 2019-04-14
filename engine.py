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
