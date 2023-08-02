from bisect import bisect_left

def g(p):
    print(p)
    return(p)

class TaskJ:
    def __init__(self) -> None:
        self.d = []

    def get(self, s):
        self.d.append([s[0]])
        for i in range(1, len(s)):
            k = bisect_left(self.d, s[i], key=g)
            if k >= len(self.d):
                self.d.append(self.d[-1] + [s[i]])
            else:
                if k == 0:
                    self.d[k] = [s[i]]
                else:
                    self.d[k] = self.d[k - 1] + [s[i]]
            print(self.d, i, s[i])
        return self.d


j = TaskJ()
j1 = j.get([3, 5, 29, 4, 5, 2, 3, 28, 7, 10, 42, 12])
print(j.d, len(j.d))