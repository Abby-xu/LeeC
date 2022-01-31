class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_amt = sum(accounts[0])
        for i in range(1, len(accounts)):
            if sum(accounts[i]) > max_amt: max_amt = sum(accounts[i])
        return max_amt
