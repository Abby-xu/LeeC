class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        if num == [0] and k == 0: return [0] 
        x = 0
        out = []
        for i in num:
            x = x*10 + i 
        x += k
        while x > 0:
            out.append(x % 10)
            x //= 10
        return out[::-1]
