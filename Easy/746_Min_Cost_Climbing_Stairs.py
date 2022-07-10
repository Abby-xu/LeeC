class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2: return cost[0]

        dp = [0 for _ in range(len(cost) + 1)]
        dp[0], dp[1] = cost[0], cost[1]
        cost = cost + [0]

        for i in range(2, len(dp)): dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return dp[-1]