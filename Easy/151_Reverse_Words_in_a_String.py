class Solution:
    def reverseWords(self, s: str) -> str:
        str_l = s.strip().split()
        return " ".join(str_l[::-1])
