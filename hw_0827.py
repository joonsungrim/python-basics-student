# 1971번
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if len(edges) == 0:
            return True
        a = {}
        for i in edges:
            if i[0] in a:
                a[i[0]].append(i[1])
            if i[0] not in a:
                a[i[0]] = [i[1]]
            if i[1] in a:
                a[i[1]].append(i[0])
            if i[1] not in a:
                a[i[1]] = [i[0]]
        return self.validPath_recursive(source,[],a,destination)
    def validPath_recursive(self,node,visited,a,destination):
        if node not in visited:
            visited.append(node)
            for neighbor in a[node]:
                self.validPath_recursive(neighbor,visited,a,destination)
        if destination in visited:
            return True
        return False