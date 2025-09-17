# Lonely photo (Time limited Exceeded)
def solve():
    b = 0
    N = int(input())
    T = input()
    i = 3
    a = 0
    while len(T[a:a+i]) < N:
        if T[a:a+i].count('G') == 1 or T[a:a+i].count('H') == 1:
            b += 1
        a += 1
        if a+i > N:
            i += 1
            a = 0
    if T.count('G') == 1 or T.count('H') == 1:
        b += 1
    return b
print(solve())

# Herdle (Accept)
b = []
for _ in range(6):
    a = input()
    c = list(a)
    b.extend(c)
d = b[:9]
e = b[9:]
f = 0
g = 0
h = 9
while f < h:
    if d[f] == e[f]:
        g += 1
        del d[f]
        del e[f]
        h -= 1
        f -= 1
    f += 1
j = 0
for i in d:
    if i in e:
        j += 1
        e.remove(i)
print(g)
print(j)

# Photoshoot (Fail)
a = int(input())
b = input()
c = []
for i in range(a):
    if i % 2 == 1:
        c.append(i)