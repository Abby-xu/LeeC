class Solution:
    def countSubstrings(self, S: str) -> int:
        N = len(S)
        ans = 0
        for center in range(2*N - 1):
            left = int(center / 2)
            right = int(left + center % 2)
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
        return ans
