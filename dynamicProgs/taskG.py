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
        if n >= 1:
            a = self.m1_or_m2(1, 1)
            b = MAX_V
            self.ex.append([a, b, min(a, b)])
        if n >= 2:
            a = MAX_V
            b = self.m1_or_m2(2, 2)
            self.ex.append([a, b, min(a, b)])
        if n >= 3:
            a = self.m1_or_m2(3, 1) + self.ex[3-1-2][2]
            b = MAX_V
            self.ex.append([a, b, min(a, b)])
        for i in range (4, n+1):
            a = self.m1_or_m2(n, 1) + self.ex[n-1-2][2]
            b = self.m1_or_m2(n, 2) + self.ex[n-1-3][2]
            self.ex.append([a, b, min(a, b)])
            
        
        
        return self.ex[n - 1][2]

    
    def m1_or_m2(self, n, m):
        return self.coords[n] - self.coords[n-m]
        

# s = [0, 2, 5, 12]
s = [0, 2, 5, 12, 15, 23]
a = taskG(s)
print(a.get())
