class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        out = 0
        for n in patterns:
            if not (word.find(n) == -1):
                out += 1
        return out