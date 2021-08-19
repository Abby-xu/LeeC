class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dp(i):
            if i == -1: return 1
            out = 0
            if s[i] > '0':
                out += dp(i-1)
            if i >= 1 and '10' <= s[i-1:i+1] <= '26':
                out += dp(i-2)
            return out
        return dp(len(s)-1)
