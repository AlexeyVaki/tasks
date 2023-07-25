class TaskJ:
    def __init__(self) -> None:
        self.d = {}

    def get(self, s):
        self.d[0] = [s[0]]
        for i in range(1, len(s)):
            p = True
            for k in self.d.keys():
                if self.d[k][-1] > s[i]:
                    self.d[k] = self.d[k - 1] + [s[i]]
                    p = False
                if self.d[k][-1] == s[i]:
                    p = False
            if p:
                self.d[len(self.d.keys())] = self.d[len(self.d.keys()) - 1] + [s[i]]
        return self.d


j = TaskJ()
j1 = j.get([3, 29, 5, 5, 5, 5, 28, 7, 10, 42, 12])
print(j.d, len(j.d))