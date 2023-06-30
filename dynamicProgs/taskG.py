MAX_V = 1e100

class taskG:
    
    def __init__(self, s) -> None:
        self.coords = s
        self.ex = []
        # в self.ex[n] хранится мин. длина для n + 2 гвоздей

    def get(self):
        if not self.ex:
             self.calc()
        return self.ex[-1][2]

    def calc(self):
        n = len(self.coords) - 1
        if n < 0:
            return 0
        elif n == 0:
            return MAX_V
        if n >= 1:
            a = self.m1_or_m2(1, 1)
            b = MAX_V
            self.ex.append([a, b, min(a, b)])
        if n >= 2:
            a = MAX_V
            b = self.m1_or_m2(2, 2)
            self.ex.append([a, b, min(a, b)])
        if n >= 3:
            a = self.m1_or_m2(3, 1) + self.ex[0][2]
            b = MAX_V
            self.ex.append([a, b, min(a, b)])
        for i in range (4, n+1):
            self.cycle(i)
        


    def cycle(self, n):
        a = self.m1_or_m2(n, 1) + self.ex[n-3][2]
        b = self.m1_or_m2(n, 2) + self.ex[n-4][2]
        self.ex.append([a, b, min(a, b)])

    def m1_or_m2(self, n, m):
        return self.coords[n] - self.coords[n-m]
        

# s = [0, 2, 5, 12]
s = [0, 2, 5, 12, 15, 23, 25, 107]
a = taskG(s)
print(a.get())
print(a.get())
print(a.ex)