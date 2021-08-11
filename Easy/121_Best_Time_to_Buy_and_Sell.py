class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = high = 0
        low = prices[0]
        bought = False
        for i in prices:
            if i <= low: 
                low = i
                bought = True
                high = 0
                continue
            if bought:
                if i > high and i - low > profit:
                    high = i
                    profit = high - low
            print(low, high, profit)
        return profit