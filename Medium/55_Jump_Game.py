class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_pos = 0
        i = 0
        while i <= max_pos:
            max_pos = max(max_pos, i + nums[i])
            if max_pos >= n-1: return True
            i += 1
        return False
