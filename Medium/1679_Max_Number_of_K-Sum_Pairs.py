class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        seen = defaultdict(int)
        for b in nums:
            a = k - b # Explain: a + b = k  =>  a = k - b
            if seen[a] > 0:
                ans += 1
                seen[a] -= 1
            else:
                seen[b] += 1
        return ans
