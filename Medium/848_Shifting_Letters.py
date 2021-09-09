class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        for i in range(len(shifts)-2, -1, -1):
            shifts[i] += shifts[i+1]
        out = []
        for j in range(len(s)):
            # shift = shifts[j] % 26
            out.append(chr((ord(s[j]) - ord('a') + shifts[j]) % 26 + ord('a')))
        return ''.join(out)
