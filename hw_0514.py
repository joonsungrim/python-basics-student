# 1018번 (실패)
a = list(map(int,input().split()))
c = []
for i in range(a[0]):
    b = input()
    c.extend(b)
e = []
for i in range(a[1] - 7):
    for j in range(a[0] - 7):
        d = i + (j * a[1])
        e.append(d)
e.sort()
f = []
g = []
z = 0
for i in e:
    for j in range (0,8):
        f.extend(c[(j * a[1]) + i:(j * a[1]) + i + 8])
    g.append(f)
    f = []
l = 0
m = 0
n = []
o = []
for i in g:
    for k in range(64):
        if (k//8) % 2 == 0 and k % 2 == 0 and i[k] == 'B':
            l += 1
        if (k//8) % 2 == 1 and k % 2 == 1 and i[k] == 'B':
            l += 1
        if (k//8) % 2 == 0 and k % 2 == 1 and i[k] == 'W':
            l += 1
        if (k//8) % 2 == 1 and k % 2 == 0 and i[k] == 'W':
            l += 1
        if (k//8) % 2 == 0 and k % 2 == 0 and i[k] == 'B':
            m += 1
        if (k//8) % 2 == 1 and k % 2 == 1 and i[k] == 'B':
            m += 1
        if (k//8) % 2 == 0 and k % 2 == 1 and i[k] == 'W':
            m += 1
        if (k//8) % 2 == 1 and k % 2 == 0 and i[k] == 'W':
            m += 1
    h = min(l,m)
    o.append(h)
    l = 0
    m = 0
print(min(o))

# 19532번 (실패)
a = list(map(int,input().split()))
e = a[0] * a[3]
f = a[1] * a[3]
g = a[2] * a[3]
h = a[3] * a[0]
i = a[4] * a[0]
j = a[5] * a[0]
k = f - i
l = g - j
y = l / k
x = (g - (f * y))/e
print(int(x),int(y))