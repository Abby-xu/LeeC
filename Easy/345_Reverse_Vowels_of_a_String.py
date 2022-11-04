class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0; right = len(s)-1
        vocab_l = list('aeiouAEIOU')
        while left < right:
            if s[left] not in vocab_l: left += 1
            if s[right] not in vocab_l: right -= 1
            if s[left] in vocab_l and s[right] in vocab_l:
                s[left], s[right] = s[right], s[left]
                left, right = left + 1, right - 1
        return ''.join(s)
