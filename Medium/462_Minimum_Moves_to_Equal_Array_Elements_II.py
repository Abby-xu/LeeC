class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = sorted(nums)[int(len(nums) / 2)]
        return sum(abs(num - median) for num in nums)