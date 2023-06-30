class taskC:
    def __init__(self):
        self.c = [[1, 0, 0, 2]]
    
    def get(self, n):
        if n <= 0:
            return 0
        if len(self.c) <=1:
            for i in range(1, n):
                self.cycle(i)
        return self.c[-1][-1]

    def cycle(self, n):
            c0 = self.c[n-1][0]
            c1 = self.c[n-1][1]
            c2 = self.c[n-1][2]
            s = [(c0 + c1), (c0 + c2), (c0), (2 * (c0 + c1) + (c0 + c2) + (c0))]
            self.c.append(s)        

n = 8
a = taskC()
print(a.get(n))
print(a.get(n))
print(a.c)