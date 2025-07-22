# 3번
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        while current.next:
            current.val = 'abc'
            if current.next.val == 'abc':
                return True
            current = current.next
        return False