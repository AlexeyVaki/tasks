class taskF:
    
    def __init__(self, s) -> None:
        self.reca = s

    def get(self):
        n=0
        now = 'L'
        while self.reca:
            if now not in self.reca:
                for i in self.reca:
                    if i == 'B':
                        n += 1
                break
            if now == 'L':
                s1 = self.reca[:self.reca.find('L')]
                self.reca = self.reca[self.reca.find('L'):]
                now = 'R'
                n += 1
            elif now == 'R':
                s1 = self.reca[:self.reca.find('R')]
                self.reca = self.reca[self.reca.find('R'):]
                now = 'L'
                n += 1
            for i in s1:
                if i == 'B':
                    n += 1
        return n



s = 'LLBLRRBRL'
a = taskF(s)
print(a.get())