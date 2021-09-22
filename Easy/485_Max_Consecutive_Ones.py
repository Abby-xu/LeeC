class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        out = 0
        curr = 0
        for i in nums:
            if i == 0:
                curr = 0
            else:
                curr += 1
                out = max(out, curr)
        return out
