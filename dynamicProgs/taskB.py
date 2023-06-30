class A:
    def __init__(self):
        self.c = [0, 1, 2, 4]
    
    def get(self, n):
        if n < 0:
            return 0
        if n < len(self.c):
            return self.c[n]
        self.c.append(self.get(n-3) + self.get(n-2) + self.get(n-1))
        return self.c[n]

        
a = A()
print([a.get(i) for i in range(1,17)])