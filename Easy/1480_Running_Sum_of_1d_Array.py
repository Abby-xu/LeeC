class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = [nums[0]]
        sum = nums[0]
        for i in range(1, len(nums)):
            sum+=nums[i]
            out.append(sum)
        return out
