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