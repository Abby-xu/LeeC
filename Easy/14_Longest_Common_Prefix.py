class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = min(strs, key=len)
        for i in strs:
            for j in range(len(out)):
                if not i[j] == out[j]: 
                    out = out[:j]
                    break
        return out
