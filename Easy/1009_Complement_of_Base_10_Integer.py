class Solution:
    def bitwiseComplement(self, n: int) -> int:
        X = 1
        while n > X: X = X * 2 + 1
        return X - n
