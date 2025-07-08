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
                self.isSameTree(p.left,q.left)
            else:
                return False
        if p.right or q.right:
            if p.right and q.right:
                self.isSameTree(p.right,q.right)
            else:
                return False
        return True

# 101번
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        l = root.left
        r = root.right
        return self.isSymmetric_recursive(l,r)
    def isSymmetric_recursive(self,lnode,rnode):
        if lnode.val != rnode.val:
            return False
        if lnode.left or rnode.right:
            if lnode.left and rnode.right:
                self.isSymmetric_recursive(lnode.left,rnode.right)
            else:
                return False
        if lnode.right or rnode.left:
            if lnode.right and rnode.left:
                self.isSymmetric_recursive(lnode.right,rnode.left)
            else:
                return False
        return True