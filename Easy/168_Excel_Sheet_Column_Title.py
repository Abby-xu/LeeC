class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # return "" if num == 0 else self.convertToTitle((num - 1) / 26) + chr((num - 1) % 26 + ord('A')) # recursive
        letters = 'ABCDEFGHIJKLMNOPQRSTUPWXYZ'
        out = ''
        n = columnNumber
        while n:
            n -= 1
            out = letters[n % 26] + out
            n //= 26
        return out
