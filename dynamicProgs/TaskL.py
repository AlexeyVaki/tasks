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
            b_l = bisect_left([i[-1] for i in self.d], s[i])
            if b_l == 0:
                self.d[0] == [s[i]] 
            elif b_l < len(self.d):
                self.d[b_l] = self.d[b_l - 1] + [s[i]]
            else:
                self.d.append(self.d[-1] + [s[i]])
            print(self.d, i, s[i])
        return self.d


j = TaskJ()
j1 = j.get([3, 5, 29, 4, 5, 2, 3, 28, 7, 10, 42, 12])
print(j.d, len(j.d))
