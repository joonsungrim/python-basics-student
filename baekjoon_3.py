# 2501번
c = input().split()
b = int(c[0])
d = int(c[0])
f = int(c[1])
e = []
while d > 0:
    if b % d == 0:
        e.append(d)
        d -= 1
    else:
        d -= 1
g = e.reverse()
if len(e) >= f:
    print(e[f - 1])
else:
    print(0)

# 9506번
a = ''
b = []
while a != -1:
    a = int(input())
    b.append(a)
    c = b[:-1]
e = []
for i in c:
    d = i
    while d > 0:
        if i % d == 0:
            e.append(d)
            d -= 1
        else:
            d -= 1
    if d == 0:
        e.reverse()
        f = e.pop()
        if sum(e) == f:
            print(f,'= ',end='')
            for i in e:
                if i != e[-1]:
                    print(i,'+',end=' ')
                else:
                    print(i)
        else:
            print(f,'is NOT perfect.')
        del e[:]

# 1978번
a = int(input())
b = []
f = 0
while len(b) < a:
    c = input().split()
    b.extend(c)
    d = list(map(int,b))
for i in d:
    e = i
    g = 0
    while e > 1:
        if i % e == 0:
            e -= 1
            g += 1
        else:
            e -= 1
    if g == 1:
        f += 1
print(f)