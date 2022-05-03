class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        start, end = -1, 0
        left_prev, right_prev = nums[0], nums[start]

        for i in range(1, len(nums)):
            # find the largest index not in place
            if nums[i] < left_prev:
                end = i
            else:
                left_prev = nums[i]

            # find the smallest index not in place
            if right_prev < nums[~i]:
                start = ~i
            else:
                right_prev = nums[~i]

        if end != 0:
            return end - (len(nums) + start) + 1
        else: 
            return 0
