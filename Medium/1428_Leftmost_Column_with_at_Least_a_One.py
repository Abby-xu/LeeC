# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        N, M = binaryMatrix.dimensions()
        r, c = 0, M-1
        out = -1
        while r < N and c >= 0:
            if binaryMatrix.get(r, c) == 1:
                out = c
                c -= 1
            else:
                r += 1
        return out
