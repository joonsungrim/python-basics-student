# 1269번
a = input()
b = input().split()
c = input().split()
d = []
e = []
for i in b:
    d.append(i)
for i in c:
    e.append(i)
print(len(set(d)-set(e)) + len(set(e)-set(d)))

# 1620번
a = list(map(int,input().split()))
c = []
d = 1
for i in range(a[0]):
    b = input()
    c.append(b)
    c.append(str(d))
    d += 1
for i in range(a[1]):
    e = input()
    f = c.index(e)
    if f % 2 == 0:
        print(c[f + 1])
    else:
        print(c[f - 1])