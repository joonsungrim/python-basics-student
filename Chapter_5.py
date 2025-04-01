class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#100.
from typing import Optional
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p.val != None and q.val == None:
            return False
        if p.val == None and q.val != None:
            return False
        if p.left != None and q.left == None:
            return False
        if p.left == None and q.left != None:
            return False
        if p.right != None and q.right == None:
            return False
        if p.right == None and q.right != None:
            return False
        if p.left.val != q.left.val:
            return False
        if p.right.val != q.right.val:
            return False
        else:
            return True

# 101.
from typing import Optional
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if root.left != None and root.right == None:
            return False
        if root.left == None and root.right != None:
            return False
        if root.left.right != None and root.right.left == None:
            return False
        if root.left.right == None and root.right.left != None:
            return False
        if root.left.left != None and root.right.right == None:
            return False
        if root.left.left == None and root.right.right != None:
            return False
        if root.left.val != root.right.val:
            return False
        if root.left.right.val != root.right.left.val:
            return False
        if root.left.left.val != root.right.right.val:
            return False
        else:
            return True