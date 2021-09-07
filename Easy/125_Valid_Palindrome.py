class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ### method 1 / O(N) ###
        out = []
        for char in s:
            if char.isalnum():
                out .append(char.lower())
        return out == out[::-1]
        
        ### method 2 / O(N) two pointers ###
        i, j = 0, len(s)-1
        while j > i:
            while j > i and not s[i].isalnum():
                i += 1
            while j > i and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
