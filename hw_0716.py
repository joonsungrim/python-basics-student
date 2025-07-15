# 100번
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p.val != q.val:
            return False
        if p.left or q.left:
            if p.left and q.left:
                if p.left.val == q.left.val:
                    return True
                else:
                    return False
            else:
                return False
        if p.right or q.right:
            if p.right and q.right:
                if p.right.val == q.right.val:
                    return True
                else:
                    return False
            else:
                return False
        return True