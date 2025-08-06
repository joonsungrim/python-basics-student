# 2974번
import heapq
class Solution:
    def numberGame(self, nums):
        nums.sort()
        heapq.heapify(nums)
        a = (len(nums)) - (len(nums) % 2) - 1
        b = 0
        while b < a:
            nums[b],nums[b+1] = nums[b+1],nums[b]
            b += 2
        
        return nums

# 2357번
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        nums.sort()
        a = 0
        b = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                pass
            else:
                b.append(nums[i])
        b.append(nums[len(nums)-1])
        if b[0] == 0:
            b.remove(0)
        return len(b)