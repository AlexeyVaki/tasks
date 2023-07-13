class taskM:
    def __init__(self) -> None:
        self.tl = TaskLab()
        self.s1 = []
        for _ in range(len(self.tl.s)):
            self.s1.append([-1 for _ in range(len(self.tl.s[0]))])
        self.s1[0][0] = 1
        self.s2 = []
        for _ in range(len(self.tl.s)):
            self.s2.append([0 for _ in range(len(self.tl.s[0]))])
        self.s2[0][0] = 1

        # Теперь s1 - доска такой же длинны и ширины, что и s.
        # Вся доска заполнена нулями, в левом верхнем углу стоит 1.

    def _get(self, p):
        if self.s1[p[0]][p[1]] >= 0:
            return self.s1[p[0]][p[1]]
        summ = 0
        for i in self.tl.getPrev(p):
            summ += self._get(i)
        self.s1[p[0]][p[1]] = summ
        return summ

    def _get2(self, p):
        if self.s2[p[0]][p[1]] >= 1:
            return self.s2[p[0]][p[1]]
        ss = []
        for i in self.tl.getPrev2(p):
            ss.append(self._get2(i))
        m = min(ss) + self.tl.s[p[0]][p[1]]
        self.s2[p[0]][p[1]] = m
        return m

    def res(self):
        t = self._get((len(self.s1) - 1, len(self.s1[0]) - 1))
        t2 = self._get2((len(self.s1) - 1, len(self.s1[0]) - 1))
        return t2


class TaskLab:
    def __init__(self) -> None:
        self.s = [
            [1, 2, 2, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 2, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1]
        ]
    
    def getNext(self, c):
        p = []
        if c[1] + 1 <= len(self.s[0]) - 1:
            if self.s[c[0]][c[1] + 1] == 1:
                p.append((c[0], c[1] + 1))
        if c[0] + 1 <= len(self.s) - 1:
            if self.s[c[0] + 1][c[1]] == 1:
                p.append((c[0] + 1, c[1]))
        return p

    def getPrev(self, c):
        p = []
        if c[1] - 1 >= 0:
            if self.s[c[0]][c[1] - 1] == 1:
                p.append((c[0], c[1] - 1))
        if c[0] - 1 >= 0:
            if self.s[c[0] - 1][c[1]] == 1:
                p.append((c[0] - 1, c[1]))
        return p

    def getPrev2(self, c):
        p = []
        if c[1] > 0:
            p.append((c[0], c[1] - 1))
        if c[0] > 0:
            p.append((c[0] - 1, c[1]))
        return p

m = taskM()
print(m.res())