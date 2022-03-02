class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        pos = 0
        for ch in t:
            if ch == s[pos]:
                pos += 1
                if pos == len(s):
                    return True
        return False
