class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0: return False
        if n == 1: return True 
        if n%4 == 0:
            return ((n-1 & n) == 0) and (n%10 == 4 or n%10 == 6)
        return False