# 10811번
N, M = map(int, input().split())
a = list(range(1, N + 1))
for _ in range(M):
    i, j = map(int, input().split())
    a[i - 1:j] = a[i - 1:j][::-1]
print(a)

# 10813번
N, M = map(int, input().split())
a = list(range(1, N + 1))
for _ in range(M):
    i, j = map(int, input().split())
    a[i-1], a[j-1] = a[j-1], a[i-1]
print(a)