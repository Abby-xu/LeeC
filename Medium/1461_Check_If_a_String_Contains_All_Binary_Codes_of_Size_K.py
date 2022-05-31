class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        return len({s[i:i+k] for i in range(len(s)-k+1)}) == 2 ** k     
