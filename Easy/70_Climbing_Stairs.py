class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(n):
            if n in memo: return memo[n]
            if n < 0: return 0
            if n == 0: return 1

            count_1 = dp(n - 1)
            count_2 = dp(n - 2)
            memo[n] = count_1 + count_2
            return memo[n]

        return dp(n)