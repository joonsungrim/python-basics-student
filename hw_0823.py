# 1791번
class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        a = []
        for i in edges:
            a.append(i[0])
            a.append(i[1])
        a.sort()
        b = [['a']]
        for i in range(len(a)):
            if i != len(a) - 1:
                if a[i] == a[i + 1]:
                    b[-1].append('a')
                else:
                    b.append(['a'])
        c = []
        for i in b:
            c.append(len(i))
        d = max(c)
        e = c.index(d) + 1
        return e

# 1971번
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if len(edges) == 0:
            return True
        a = []
        for i in range(n):
            b = []
            for j in edges:
                if j[0] == i:
                    b.append(j[1])
                if j[1] == i:
                    b.append(j[0])
            a.append(b)
        return self.validPath_recursive(a,0,n)
    def validPath_recursive(self,a,b,n):
        if n - 1 in a[b]:
            return True
        for i in a:
            if b in i:
                i.remove(b)
        for i in a[b]:
            self.validPath_recursive(a,i,n)
        return False