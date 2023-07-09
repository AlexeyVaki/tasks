class taskM:
    def __init__(self) -> None:
        self.s = [
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1]
        ]
        self.s1 = []
        for _ in range(len(self.s)):
            self.s1.append([0 for _ in range(len(self.s[0]))])
        self.s1[0][0] = 1

        # Теперь s1 - доска такой же длинны и ширины, что и s.
        # Вся доска заполнена нулями, в левом верхнем углу стоит 1.

    def get(self):
        for i in range(len(self.s1)):
            for j in range(len(self.s1[0])):
                if j != len(self.s1[0]) - 1:
                    if self.s[i][j + 1] == 1:
                        self.s1[i][j + 1] += self.s1[i][j]
                if i != len(self.s1) - 1:
                    if self.s[i + 1][j] == 1:
                        self.s1[i + 1][j] += self.s1[i][j]
        return self.s1[-1][-1]


m = taskM()
print(m.get())