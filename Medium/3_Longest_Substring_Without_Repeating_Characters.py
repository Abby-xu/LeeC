class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res, last_match = 0, -1
        for i, c in enumerate(s):
            if c in dic and last_match < dic[c]:
                last_match = dic[c]
            res = max(res, i - last_match)
            dic[c] = i
        return res