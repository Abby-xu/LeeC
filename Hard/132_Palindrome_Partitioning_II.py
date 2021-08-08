class Solution:
    def minCut(self, s: str) -> int:
        @lru_cache(None)
        def isPalindrome(l,r): # O(N^2)
            if l >= r: return True
            if s[l] != s[r]: return False
            return isPalindrome(l+1, r-1)
        
        @lru_cache(None)
        def dp(i):
            if i == len(s): return 0
            out = math.inf
            for j in range(i, len(s)):
                if (isPalindrome(i, j)):
                    out = min(out, dp(j + 1) + 1)
            return out
        
        return dp(0) - 1