# 1316번
N = input()
a = int(N)
c = 0
for _ in range(a):
    i = input()
    j = list(i)
    b = 0
    while b < len(j) - 1:
        if j[b] == j[b + 1]:
            j.pop(b + 1)
        else:
            b += 1
    if len(set(j)) == len(j):
        c += 1
print(c)

# 25206번
e = 0
f = 0
for _ in range(20):
    a = input()
    b = a.split()
    c = b[1:]
    d = int(float(c[0]))
    if c[1] == 'A+':
        e = e + (d * 4.5)
        f += d
    elif c[1] == 'A0':
        e = e + (d * 4.0)
        f += d
    elif c[1] == 'B+':
        e = e + (d * 3.5)
        f += d
    elif c[1] == 'B0':
        e = e + (d * 3.0)
        f += d
    elif c[1] == 'C+':
        e = e + (d * 2.5)
        f += d
    elif c[1] == 'C0':
        e = e + (d * 2.0)
        f += d
    elif c[1] == 'D+':
        e = e + (d * 1.5)
        f += d
    elif c[1] == 'D0':
        e = e + (d * 1.0)
        f += d
    elif c[1] == 'F':
        e = e + (d * 0.0)
        f += d
    else:
        continue
print(e/f)

# 2738번
c = []
N, M = map(int, input().split())
for _ in range (N * 2):
    a = input()
    b = list(map(int, a.split()))
    c.extend(b)
d = 0
while d < (N * M):
    e = c[d] + c[d + (N * M)]
    if ((d + 1) % 3) != 0:
        print(e, end = ' ')
        d += 1
    else:
        print(e)
        d += 1

# 2566번
b = []
for _ in range(9):
    a = list(map(int, input().split()))
    b.extend(a)
print(max(b))
c = max(b)
print ((b.index(c) + 1) // 9 + 1, end=' ')
print ((b.index(c) + 1) % 9)