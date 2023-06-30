class taskC:
    def __init__(self):
        self.c = [[1, 0, 0, 2]]
        # c[n, 0] - 00/01; 
        # c[n, 1] - 10; 
        # c[n, 2] - 11; 
        # c[n, 3] - сумма
    
    def get(self, n):
        if n <= 0:
            return 0
        for i in range(len(self.c), n):
            self.cycle(i)
        return self.c[n - 1][-1]

    def cycle(self, n):
            c0 = self.c[n-1][0]
            c1 = self.c[n-1][1]
            c2 = self.c[n-1][2]
            s = [(c0 + c1), (c0 + c2), (c0), (2 * (c0 + c1) + (c0 + c2) + (c0))]
            self.c.append(s)        

n = 8
a = taskC()
print(a.get(n))
print(a.get(10))
print(a.get(2))
print(a.c)