# 10773번
a = int(input())
c = []
d = 0
while d < a:
    b = int(input())
    c.append(b)
    if c[d] != 0:
        d += 1
    else:
        c.pop()
        c.pop()
        d -= 1
        a -= 2
if len(c) == 0:
    print(0)
else:
    print(sum(c))

# 2164번
a = int(input())
b = []
for i in range(a):
    b.append(i + 1)
c = 0
while len(b) > 1:
    if c % 2 == 0:
        b.pop(0)
        c += 1
    else:
        b.append(b[0])
        b.pop(0)
        c += 1
print(b[0])