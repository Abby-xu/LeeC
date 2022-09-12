class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r, score = 0, len(tokens) - 1, 0
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
            elif score and l != r:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break
        return score