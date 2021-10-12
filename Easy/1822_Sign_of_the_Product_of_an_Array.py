class Solution:
    def arraySign(self, nums: List[int]) -> int:
        out = 1 # default positive
        for num in nums:
            if num == 0: return 0
            if num < 0:
                out *= -1
        return out
