MAX_V = 1e100

class taskG:
    
    def __init__(self, s) -> None:
        self.coords = s
        self.ex = []

    def get(self):
        return self.calc(len(self.coords) - 1)

    def calc(self, n):
        if n < 0:
            return 0
        if len(self.ex) > n:
            None
        elif n == 0:
            self.ex.append([MAX_V, MAX_V, MAX_V])
        elif n == 1:
            a = self.m1_or_m2(n, 1)
            b = MAX_V
            self.ex.append([a, b, min(a, b)])
        elif n == 2:
            a = MAX_V
            b = self.m1_or_m2(n, 2)
            self.ex.append([a, b, min(a, b)])
        
        
        return self.ex[n - 1][2]

    
    def m1_or_m2(self, n, m):
        return self.coords[n] - self.coords[n-m]
        

# s = [0, 2, 5, 12]
s = [0, 2, 5]
a = taskG(s)
print(a.get())