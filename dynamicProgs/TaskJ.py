class TaskJ:
    def __init__(self) -> None:
        self.d = {}

    def get(self, s):
        self.d[0] = [s[0]]
        for i in range(1, len(s)):
            m = []
            for j in range(len(self.d)):
                if s[j] < s[i]:
                    if len(self.d[j]) > len(m):
                        m = self.d[j].copy()
                    
            m += [s[i]]
            self.d[i] = m
        return max(self.d, key=self.p)

    def p(self, k):
        return len(self.d[k])

j = TaskJ()
j1 = j.get([3, 29, 5, 5, 28, 7])
print(j.d)
print(j.d[j1])