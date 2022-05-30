class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sig = (dividend < 0) == (divisor < 0)
        dividend, divisor, res = abs(dividend), abs(divisor), 0
        while dividend >= divisor:
            x = 0
            while dividend >= divisor << (x + 1): x += 1
            res += 1 << x
            dividend -= divisor << x
        return min(res if sig else -res, 2147483647)