# 108번
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        n = 0
        while n != mid:
            if n == 0:
                root.left = TreeNode(nums[n])
            else:
                root.right = TreeNode(nums[n])
            n += 1
        m = 0
        while m != len(nums) - 1:
            root.right = TreeNode(nums[mid+m])
            m += 1
        return root

# 637번
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        a = [[root.val]]
        return self.averageOfLevels_recursive(root,a)
    def averageOfLevels_recursive(self,root,a):
        b = []
        if root.left or root.right:
            a.append(b)
            if root.left:
                b.append(root.left.val)
                self.averageOfLevels_recursive(root.left,a)
            if root.right:
                b.append(root.right.val)
                self.averageOfLevels_recursive(root.right,a)
        c = []
        for i in range(len(a)):
            j = sum(a[i])
            c.append(j/len(a[i]))
        return c