from bisect import bisect_left

s = [1, 4, 7, 10, 32]
inp = 6
while inp != 'stop':
    inp = int(inp)
    if inp in s:
        print(s)
    else:
        b_l = bisect_left(s, inp)
        print(b_l)
        if b_l >= len(s):
            s.append(inp)
        else:
            s[b_l] = inp
        print(s)
    inp = input()
    