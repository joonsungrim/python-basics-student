# 637번
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        a = [[0.00000,root.val]]
        return self.averageOfLevels_recursive(root,a,0)
    def averageOfLevels_recursive(self,root,a,c):
        c += 1
        b = []
        a.append(b)
        b.append(c)
        if root.left or root.right:
            if root.left:
                b.append(root.left.val)
                self.averageOfLevels_recursive(root.left,a,c)
            if root.right:
                b.append(root.right.val)
                self.averageOfLevels_recursive(root.right,a,c)
        for i in a:
            if len(i) <= 1:
                a.remove(i)
        e = []
        for _ in range(int(a[-1][0] + 1)):
            e.append([])
        for i in a:
            e[int(i[0])].append(i[1:])
        for i in e:
            for j in i:
                i.append(sum(j)/len(j))
                i.remove(j)
        f = []
        for i in e:
            for j in i:
                f.append(j)
        return f

# 108번
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        if len(nums) == 1:
            return root
        return self.sortedArrayToBST_recursive(root,nums,0)
    def sortedArrayToBST_recursive(self,root,nums,i):
        mid = len(nums) // 2
        a = mid + 1
        if i == 0:
            root.left = TreeNode(nums[i])
            i += 1
            if len(nums) > a:
                root.right = TreeNode(nums[a])
                self.sortedArrayToBST_recursive(root.right,nums,a + i)
            self.sortedArrayToBST_recursive(root.left,nums,i)
        else:
            if i < mid:
                root.right = TreeNode(nums[i])
                i += 1
                self.sortedArrayToBST_recursive(root.right,nums,i)
            if mid < i < len(nums):
                root.right = TreeNode(nums[i])
                i += 1
                self.sortedArrayToBST_recursive(root.right,nums,i)
        return root