#Q.387
s = 'a' 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = {}

        for i in s:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
        
        for j, k in enumerate(s):
            if a[k] == 1:
                return j
        
        return -1
   
x = Solution()
print(x.firstUniqChar(s))

# hash 사용
# ex) 'leetcode'
# {'l': 1}
# {'e': 3}
# {'t': 1}
# {'c': 1}
# {'o': 1}
# {'d': 1}

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

# head = [1,2,2,1]은 list가 아닌 listnode
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(1)