class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] > len(nums): nums[i] = 0
        for i in range(len(nums)):
            if 1 <= nums[i] % (len(nums) + 1) <= len(nums):
                idx = nums[i] % (len(nums) + 1) - 1
                nums[idx] += len(nums) + 1
          
        for i in range(len(nums)):
            if nums[i] <= len(nums):
                return i + 1
        
        return len(nums) + 1