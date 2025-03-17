#Q.387
s = 'a'
class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = list(s)
        for i in a:
            c = 0
            while c < len(a):
                b = s.count(s[c])
                if b == 1:
                    return c
                elif b > 1:
                    c += 1
                    continue
            return -1

x = Solution()
print(x.firstUniqChar(s))

# Q.234
head = [1,2,2,1]
from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == head[::-1]:
            return True
        else:
            return False

x = Solution()
print(x.isPalindrome(head))