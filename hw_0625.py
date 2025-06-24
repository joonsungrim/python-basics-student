# 496번
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        self.nums1 = nums1
        self.nums2 = nums2
        d = len(nums1)
        e = []
        for i in range(d):
            e.append(-1)
        f = 0
        for i in nums1:
            b = nums2.index(i)
            c = nums2[b + 1:]
            for j in c:
                if j > i:
                    del(e[f])
                    e.insert(f,j)
                    break
                else:
                    continue
            f += 1
        return e
x = Solution()
print(x)

# 2073번
class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        self.tickets = tickets
        self.k = k
        a = tickets[k]
        b = 0
        for i in range(len(tickets)):
            if tickets[i] < a:
                b += tickets[i]
            elif tickets[i] >= a and i > k:
                b += (a - 1)
            else:
                b += a
        return b
x = Solution()
print(x)