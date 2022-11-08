class Solution:
    def makeGood(self, s: str) -> str:
        out = []
        for c in s:
            if out and out[-1] == c.swapcase():
                out.pop()
            else:
                out.append(c)
        return ''.join(out)
