class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = zeros = 0
        out = 0
        for c in s:
            if c == '1': 
                ones += 1
            else:
                if ones:
                    zeros += 1
                    if zeros == ones: 
                        out += ones
                        ones = zeros = 0
        out += zeros
        return out