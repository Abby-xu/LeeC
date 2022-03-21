class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        sizes = []
        while s:
            i = 1
            while set(s[:i]) & set(s[i:]):
                i += 1
            sizes.append(i)
            s = s[i:]
        return sizes
