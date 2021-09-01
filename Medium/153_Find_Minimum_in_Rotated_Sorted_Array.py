class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[len(nums)-1]: return nums[0]    
        if len(nums) == 2: 
            return nums[0] if nums[0] < nums[1] else nums[1]
            
        Median = len(nums) // 2
        return self.findMin(nums[Median:]) if nums[Median] > nums[len(nums)-1] else self.findMin(nums[:Median+1])
