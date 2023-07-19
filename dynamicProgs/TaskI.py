class TaskI:
    
    def __init__(self) -> None:
        self.d = dict()
        self._prepare()

    def _prepare(self): 
        self.d[1] = 0

    def get(self, n):
        if n <= 0:
            return 0
        if n in self.d:
            return self.d[n]
        p2 = 1 + n % 2 + self.get(n // 2)
        p3 = 1 + n % 3 + self.get(n // 3)
        self.d[n] = min(p2, p3)
        return self.d[n]
        
        



t = TaskI()
tt = t.get(562340)
print(tt)