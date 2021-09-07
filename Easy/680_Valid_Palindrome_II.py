class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            #check each char
            if s[i] != s[j]:
                del_i = s[i+1:j+1]
                del_j = s[i:j]
                return del_i == del_i[::-1] or del_j == del_j[::-1]
            i += 1
            j -= 1
        return True
