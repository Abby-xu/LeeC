class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0: return
        keep_run = 0
        maximum = nums[0]
        for i in nums:
            keep_run += i
            if keep_run > maximum:
                maximum = keep_run
            if keep_run < 0:
                keep_run = 0
        return maximum