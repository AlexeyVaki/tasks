MAX_V = 1e100

class taskG:
    
    def __init__(self, s) -> None:
        self.coords = s
        self.ex = dict()
        self._prepare()

    
    def calc(self):
        return self._get(len(self.coords))

    
    def _prepare(self):
        self.ex[1] = MAX_V
        if len(self.coords) > 1:
            self.ex[2] = self.coords[1] - self.coords[0]
        if len(self.coords) > 2:
            self.ex[3] = self.coords[2] - self.coords[0]
    
    
    def _get(self, n):
        print(n)
        if n <= 0:
            return 0
        if n in self.ex:
            print(f'{n} - {self.ex[n]}')
            return self.ex[n]
        a = self._get(n-2) + self.coords[n-1] - self.coords[n-2]
        b = self._get(n-3) + self.coords[n-1] - self.coords[n-3]
        res = min(a,b)
        print(f'add {n} - {a}, {b}, {res}')
        self.ex[n] = res
        return res


# s = [0, 2, 5, 12]
s = [0, 2, 5, 12, 13, 23, 24, 29]
a = taskG(s)
print(a.calc())