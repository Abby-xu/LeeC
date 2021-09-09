class Solution:
    def removeDuplicates(self, s: str) -> str:
        out = []
        for char in s:
            if out and out[-1] == char:
                out.pop()
            else:
                out.append(char)
        return ''.join(out)
