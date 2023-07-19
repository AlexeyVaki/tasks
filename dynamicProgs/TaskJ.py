class TaskJ:
    def __init__(self) -> None:
        self.d = {0: 1}

    def get(self, s):
        for i in range(1, len(s)):
            m = 1
            for j in self.d.keys():
                if s[j] < s[i]:
                    if self.d[j] < m:
                        m = self.d[j]
                    m += 1
            self.d[i] = m
        return max(self.d.values())

j = TaskJ()
j1 = j.get([10, 11, 12, 13, 11, 12, 13, 14, 15])
print(j.d)
print(j1)



